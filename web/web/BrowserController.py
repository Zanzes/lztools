import time

from math import ceil
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .Exceptions import ElementVisibilityTimeout
from .LocatorCollection import LocatorCollection
from .HTMLElement import HTMLElement, Locator
from .HTMLElementList import HTMLElementList
from .Driver import Driver

locators = LocatorCollection()
locators["body"] = Locator("body", By.TAG_NAME)
locators["executionDisplay"] = Locator("statusblock", By.CLASS_NAME)

class BrowserController(object):
    _instance = Driver()
    
    def __init__(self, *args, **kwargs):
        self.timeout = ConfigManager["Default"].timeout_short
        super().__init__(*args, **kwargs)

    def get(self, url):
        self._instance.get(url)
        self.accept_alert()

    def get_current_url(self):
        return self._instance.current_url

    def find_mirbutton(self, data_template_value, wait=None):
        return self.wait_elements(Locator(find_target="mirbutton", by=By.CLASS_NAME), wait).by_attribute("data-template", data_template_value)

    def __wait(self, wait):
        if wait is None:
            wait = ConfigManager["Default"].timeout_short
        return WebDriverWait(self._instance, timeout=wait, poll_frequency=ConfigManager["Default"].pollfrequency)

    def find_element(self, locator):
        return HTMLElement(self._instance.find_element(locator[1], locator[0]))

    def find_elements(self, locator):
        return HTMLElementList([HTMLElement(e) for e in self._instance.find_elements(locator[1], locator[0])])

    def wait_element(self, locator, wait=None, condition=expected_conditions.presence_of_element_located):
        if wait is None:
            wait = ConfigManager["Default"].timeout_short
        elm = self.__wait(wait=wait).until(condition((locator.by, locator.find_target)), f"Timeout while waiting for element ({locator.by}: {locator.find_target})")
        return HTMLElement(elm)

    def wait_elements(self, locator, wait=None, condition=expected_conditions.presence_of_all_elements_located):
        if wait is None:
            wait = ConfigManager["Default"].timeout_short
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
        w = wait/ConfigManager["Default"].pollfrequency
        if w < 1:
            w = 1
        for i in range(int(w)):
            try:
                if self.is_element_available(locator):
                    break
            except:
                pass
            time.sleep(ConfigManager["Default"].pollfrequency)
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
            t -= ConfigManager["Default"].pollfrequency
            e = self.is_visible(locator, wait)
            if e:
                time.sleep(ConfigManager["Default"].pollfrequency)
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

        pf = ConfigManager["Default"].pollfrequency
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
            wait = ConfigManager["Default"].timeout_short
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

    def has_error(self, status=None):
        from Tools import APIModule
        if status is None:
            status = APIModule.get_robot_status()
        return status.state_text == RobotStates.Error

    def reset_error(self):
        # return self.find_element("status").click()
        self.execute_script("clear_errors(event, 'left');")

    def error_9000_workaround(self):
        from Tools import APIModule
        status = APIModule.get_robot_status()
        if self.has_error(status):
            only_9000 = True
            for error in status.errors:
                if error.code != 9000:
                    only_9000 = False
                    break
            if not only_9000:
                raise Exception("Check robot error!")
            else:
                self.reset_error()
                self.error_9000_workaround()

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

    def add_mission_to_queue(self, name):
        from Tools import APIModule
        APIModule.add_mission_to_queue(name)

    def clear_mission_queue(self):
        from Tools import APIModule
        APIModule.remove_all_missions_from_queue()

    def execute_script(self, script):
        return self._instance.execute_script(script)

    def ensure_mission_executing(self):
        from Tools import APIModule
        status = APIModule.get_robot_status()
        if not status.state_text == RobotStates.Executing:
            self.execute_script("robot_change_state(3);")
        # if not get_execution_status() == ExecutionStatus.Running:
        #     execute_script("robot_change_state(3);")

    def get_mission_queue(self):
        from Tools import APIModule
        return APIModule.get_mission_queue()

    def get_mission_queue_count(self):
        return len(self.get_mission_queue())

    def get_selected_language(self):
        text = self.wait_element(Locator("language", By.ID)).text
        return text

    def get_page_text(self):
        t = self.wait_element(locators['body']).text
        return [s for s in t.split("\n") if s and not s.isspace()]

    def set_select(self, locator, value, wait=None):
        if wait is None:
            wait = ConfigManager["Default"].timeout_short
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

    # @classmethod
    # def quit(cls):
    #     cls._instance.quit()