import time
from math import ceil

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .Driver import Driver
from .Exceptions import ElementVisibilityTimeout
from .HTMLElement import HTMLElement, Locator
from .HTMLElementList import HTMLElementList
from .LocatorCollection import LocatorCollection

locators = LocatorCollection()
locators["body"] = Locator("body", By.TAG_NAME)
locators["executionDisplay"] = Locator("statusblock", By.CLASS_NAME)

class BrowserController(object):
    _instance:webdriver.Firefox = Driver()
    
    def __init__(self, *args, **kwargs):
        self.timeout = 10
        super().__init__(*args, **kwargs)

    def get(self, url):
        self._instance.get(url)
        self.accept_alert()

    def get_current_url(self):
        return self._instance.current_url

    def __wait(self, wait):
        if wait is None:
            wait = 10
        return WebDriverWait(self._instance, timeout=wait, poll_frequency=0.3)

    def find_element(self, locator):
        return HTMLElement(self._instance.find_element(locator[1], locator[0]))

    def find_elements(self, locator):
        return HTMLElementList([HTMLElement(e) for e in self._instance.find_elements(locator[1], locator[0])])

    def wait_element(self, locator, wait=None, condition=expected_conditions.presence_of_element_located):
        if wait is None:
            wait = 10
        elm = self.__wait(wait=wait).until(condition((locator.by, locator.find_target)), f"Timeout while waiting for element ({locator.by}: {locator.find_target})")
        return HTMLElement(elm)

    def wait_elements(self, locator, wait=None, condition=expected_conditions.presence_of_all_elements_located):
        if wait is None:
            wait = 10
        elms = self.__wait(wait=wait).until(condition((locator.by, locator.find_target)), message=f"Timeout while waiting for element ({locator.by}: {locator.find_target})")
        return HTMLElementList([HTMLElement(e) for e in elms])

    def is_element_present(self, locator):
        try:
            self.wait_element(locator)
            return True
        except:
            return False

    def is_visible(self, locator, wait):
        e = self.wait_element(locator, wait)

        if e.is_displayed():
            return e
        else:
            return None

    def wait_til_stale(self, element, wait):
        return self.__wait(wait).until(expected_conditions.staleness_of(element), message=f"Timeout while waiting for element to be removed ({element.tag_name}, {element.id})")

    def get_screen_resolution(self):
        sdata = self._instance.execute_script("screen.width + 'x' + screen.height").split('x')
        width, height = (int(sdata[0]), int(sdata[1]))

        return width, height

    def clear_cache(self):
        self._instance.get('chrome://settings/clearBrowserData')
        self.wait_element(Locator("* /deep/ #clearBrowsingDataConfirm", By.CLASS_NAME))
        self._instance.find_element(Locator('* /deep/ #clearBrowsingDataConfirm', By.CLASS_NAME)).click()
        self.wait_for_element_not_present(Locator('* /deep/ #clearBrowsingDataConfirm', By.CLASS_NAME))

    def clean_cookies_and_cache(self):
        self.clear_cache()
        time.sleep(3)
        self._instance.delete_all_cookies()
        # super(webdriver.Chrome, self).delete_all_cookies()

    def is_element_available(self, locator):
        """
        Synchronization method for making sure the element we're looking for is not only on the page,
        but also visible -- since Se will happily deal with things that aren't visible.

        Use this instead of is_element_present most of the time.
        """
        if self.is_element_present(locator):
            if self.is_visible(locator, 0.5):
                return True
            else:
                return False
        else:
            return False

    def wait_for_available(self, locator, wait):
        """
        Synchronization to deal with elements that are present, and are visible

        :raises: ElementVisiblityTimeout
        """
        w = wait/0.3
        if w < 1:
            w = 1
        for i in range(int(w)):
            try:
                if self.is_element_available(locator):
                    break
            except:
                pass
            time.sleep(0.3)
        else:
            raise ElementVisibilityTimeout(f"Cant locate ({locator.find_target}: {locator.by})")
        return True

    def wait_for_hidden(self, locator, wait=None):
        """
        Synchronization to deal with elements that are present, but are visibility until some action
        triggers their hidden-ness.

        :raises: ElementVisiblityTimeout=
        """
        t = self.timeout
        while t > 0:
            t -= 0.3
            e = self.is_visible(locator, wait)
            if e:
                time.sleep(0.3)
            else:
                return
        raise Exception(f"Timeout while waiting for element ({locator.by}: {locator.find_target})")

    def create_action_chain(self):
        return ActionChains(self._instance)

    def wait_for_text(self, locator, text, wait=None):
        """
        Synchronization on some text being displayed in a particular element.

        :raises: ElementVisiblityTimeout
        """
        if wait is not None:
            w = wait
        else:
            w = self.timeout

        pf = 0.3
        ticks = w / pf

        for _ in range(int(ceil(ticks))):
            try:
                elsms = self._instance.find_elements(locator.by, locator.find_target)
                for e in elsms:
                    if e.text == text:
                        return True
            except:
                raise
                time.sleep(pf)

        raise Exception(f"Timeout while waiting for element ({locator.by}: {locator.find_target})")

    def wait_til_element_removed(self, element,  wait=None):
        self.__wait(wait).until(expected_conditions.staleness_of(element), "Timeout while waiting for element to be removed")

    def wait_for_alert(self, wait=None):
        if wait is None:
            wait = 10
        return self.__wait(wait).until(expected_conditions.alert_is_present())

    def wait_for_value_changed(self, locator, text):
        e = self.wait_element(locator)
        for i in range(self.timeout):
            try:
                if len(e.text.strip()) != 0 and e.text != text:
                    return True
            except e:
                e = self.wait_element(locator)
            finally:
                time.sleep(1)
        else:
            raise Exception("%s visibility timed out" % locator)

    def wait_for_element_not_present(self, locator):
        """
        Synchronization helper to wait until some element is removed from the page

        :raises: ElementVisiblityTimeout
        """
        for i in range(int(self.timeout)):
            if self.is_element_present(locator):
                time.sleep(1)
            else:
                break
        else:
            raise Exception("%s presence timed out" % locator)
        return True

    def cancel_alert(self,):
        self.wait_for_alert()
        self._instance.switch_to.alert.dismiss()

    def accept_alert(self, wait=None):
        if wait:
            try:
                self.wait_for_alert(wait)
            except TimeoutException:
                pass
        try:
            self._instance.switch_to.alert.accept()
        except NoAlertPresentException:
            pass

    def wait_for(self, l, op, r, exe_l=False, exe_r=False):
        if exe_l and exe_r:
            while not op(l(), r()):
                time.sleep(0.1)
        elif exe_l:
            while not op(l(), r):
                time.sleep(0.1)
        elif exe_r:
            while not op(l, r()):
                time.sleep(0.1)
        else:
            while not op(l, r):
                time.sleep(0.1)

    def wait_for_true(self, action_str, pollfrequency):
        while not eval(action_str):
            time.sleep(pollfrequency)

    def execute_script(self, script):
        return self._instance.execute_script(script)

    def get_page_text(self):
        t = self.wait_element(locators['body']).text
        return [s for s in t.split("\n") if s and not s.isspace()]

    def set_select(self, locator, value, wait=None):
        if wait is None:
            wait = 10
        sel = self.wait_element(locator, wait).to_select()
        try:
            sel.select_by_visible_text(value)
        except:
            try:
                opts = sel.options
                o = [op for op in opts if op.text == value].pop()
                sel.select_by_value(o.get_attribute("value"))
            except:
                try:
                    opts = sel.options
                    o = [op for op in opts if op.get_attribute("value") == value].pop()
                    sel.select_by_value(o.get_attribute("value"))
                except:
                    pass

    def chain_find(self, locaters):
        if isinstance(locaters[0], Locator):
            ls = locaters
        elif isinstance(locaters[0], tuple):
            ls = [Locator(t[0], t[1]) for t in locaters]
        else:
            raise Exception(f"Cant chain: {locaters}")
        e = self.wait_element(ls[0])
        for l in ls[1:]:
            e = e.find_element(l)
        return e

    def refresh(self):
        self._instance.refresh()
        self.accept_alert()

    def get_cookies(self):
        return self._instance.get_cookies()

    def add_cookie(self, cookie):
        return self._instance.add_cookie(cookie)

    def delete_all_cookies(self):
        self._instance.delete_all_cookies()