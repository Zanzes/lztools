#!  /usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium.webdriver.common.by import By

from .LocatorCollection import LocatorCollection

from .HTMLElement import Locator
from .PageBase import PageBase

url = ConfigManager["Default"].robot_ip + "/dashboards/"

locators = LocatorCollection()

class DashboardPage(PageBase):

    def __init__(self, the_id="", auto_auth=True, language_check=True):
        res = url + the_id
        super(DashboardPage, self).__init__(res, auto_auth, language_check=language_check)
        if auto_auth:
            self.wait_element(locators['pageId'])

    def open_api_login(self, the_url):
        self.wait_element(locators['sideMenu'])
        self.get(the_url)
        return self

    def open_users(self, the_url):
        self.wait_element(locators['sideMenu'])
        self.get(the_url)
        return self

    def get_widget_types(self):
        self.wait_elements(locators["dashWidgets"])
        fe = self.find_elements(locators["dashWidgets"])
        for e in fe:
            yield e.get_attribute("data-widget")

    def get_widget(self, widget_type):
        self.wait_elements(locators["dashWidgets"])
        fe = self.find_elements(locators["dashWidgets"])
        for e in fe:
            if e.get_attribute("data-widget") == widget_type:
                return e
        return None

    def has_widget(self, widget_type):
        if self.get_widget(widget_type):
            return True

    def move_to_position(self, position):
        position.click()
        try:
            self.wait_elements(locators["mapGoToBtn"])
        except:
            return
        elms = self.find_elements(locators["mapGoToBtn"])
        rs = [btn for btn in self.find_elements(locators["mapGoToBtn"]) if btn.text == "Go to"]
        for r in rs:
            r.click()
        for r in elms:
            if not r.is_stale():
                r.click()
                try:
                    self.wait_element(locators["mapPopupYesBtn"])
                    yes = self.find_element(locators["mapPopupYesBtn"])
                    if yes:
                        yes.click()
                except:
                    pass
        self.mission_wait_queue_empty()

    def mission_wait_for_complete(self, interval=2.5):
        while not self.is_mission_complete(APIModule.get_robot_status()):
            time.sleep(interval)
            self.error_9000_workaround()
            self.ensure_mission_executing()

    def mission_wait_queue_empty(self, interval=1):
        while not APIModule.get_mission_queue_length() == 0:
            time.sleep(interval)
            self.ensure_mission_executing()

    def get_mission_text(self):
        self.error_9000_workaround()
        e = self.find_element(locators["missionStatusContainer"])
        text = e.find_element(Locator("p", By.TAG_NAME)).text
        return text

    def is_mission_complete(self, status):
        return status.state_text == RobotStates.Ready

    def get_positions(self):
        try:
            self.wait_elements(locators["mapPositions"])
        finally:
            return [f for f in self.find_elements(locators["mapPositions"]) if f.is_displayed()]

    def open_default_dashboard(self):
        self.get(ConfigManager["Default"].robot_ip+"/dashboards/mirconst-guid-0000-0001-dashboards00")
        return self

    def create_position(self, name):
        map = self.wait_element(Locator("map", By.CLASS_NAME))
        height = self.execute_script("return document.getElementsByClassName('map')[0].clientHeight")
        self.create_action_chain().move_to_element(map).move_by_offset(20, int(height)/2).click(map).pause(1).move_to_element_with_offset(map, 200, int(height)/2).perform()
