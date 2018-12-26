#!  /usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path

from selenium.webdriver.common.by import By

from .Exceptions import UploadException
from .LocatorCollection import LocatorCollection
from .BrowserController import BrowserController
from .HTMLElement import Locator

locators = LocatorCollection()

class PageBase(BrowserController):
    url = None

    def __init__(self, url, auto_auth=True, language_check=True, skip=False):
        self.url = url
        self.timeout = 10
        super(PageBase, self).__init__()
        if skip:
            return
        self.navigate()

        # if language_check:
            # TranslationModule.language_verification(self.get_page_text(), self.selected_language, self.get_current_url())

    @property
    def selected_language(self):
        t = self.wait_element(Locator("language", By.CLASS_NAME)).text
        return t.capitalize()

    def logout(self):
        self.get(logout)
        self.delete_all_cookies()
        return self

    def ensure_page(self):
        if self.get_current_url() != self.url:
            self.navigate()
            self.wait_element(Locator("language", By.CLASS_NAME), 10)

    def navigate(self):
        if self.url != self.get_current_url():
            self.get(self.url)

    def get_robot_name_top_menu(self):
        name = self.wait_element(locators["headerRobotName"]).text
        return name

    def get_software_version_footer(self):
        e = self.wait_element(locators['footerContainer'])
        text = e.find_element(locators['footerSoftwareVersion']).text
        return text

    def at_login_page(self):
        try:
            x = self.wait_element(locators["loginForm"], 0.3)
            if x is not None:
                return True
        except:
            pass
        return False

    def upload_site_resource(self, name, filename):
        self.get(ConfigManager["Default"].robot_ip + u"/setup/maps")
        self.wait_for_hidden(locators["uploadFormContainer"])
        rp = get_module_path(Resources)

        path = Path(f"{rp}/{filename}").absolute()
        if not path.exists():
            raise Exception(f"File not found at {str(path)}\nCurrently in {str(Path('.').absolute())}")
        if path.is_file():
            cont = self.wait_element(locators["uploadFormContainer"])
            form = cont.find_element(locators["uploadForm"])
            the_id = form.get_attribute("id").split("_")[-1]
            inputId = f"mir_uploadbutton_{the_id}"
            self.wait_element(Locator(inputId, By.ID)).send_keys(str(path))
            box = self.wait_element(locators["popup"])
            self.wait_til_element_removed(box, 50)
            try:
                b1 = self.wait_element(locators["error_popup"], 1)
            except:
                b1 = None
            if b1 is not None:
                error_text = b1.find_element(Locator('h1', By.TAG_NAME)).text
                raise UploadException(f"Upload unsuccessful error message: {error_text}")

            self.refresh()
            self.wait_for_text(Locator("subhead", By.CLASS_NAME), name)

    def ensure_site_resource(self, name):
        m = APIModule.map_exists(name=name)
        s = APIModule.site_exists(name)
        if not m or not s:
            if m is not None:
                APIModule.delete_map(m)
            if s is not None:
                APIModule.delete_site(s)
            self.upload_site_resource(name, f"{name}.site")

    def get_mir_buttons(self):
        return self.wait_elements(locators["mirbutton"])




