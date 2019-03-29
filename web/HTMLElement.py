#!  /usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple
from datetime import datetime

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from HTMLElementList import HTMLElementList
from Position import Position

Locator = namedtuple("Locator", ["find_target", "by"])

class HTMLElement(object):
    element = None

    def __init__(self, element):
        self.element = element
        self.__dict__.update(element.__dict__)

    @property
    def text(self):
        return self.element.text
    @text.setter
    def text(self, value):
        self.element.text = value

    @property
    def position(self):
        return Position(self.element.location["x"], self.element.location["y"])
    @position.setter
    def position(self, value):
        self.element.location["x"] = value.x
        self.element.location["y"] = value.y

    @property
    def id(self):
        return self.element.id

    @property
    def tag_name(self):
        return self.element.tag_name

    def to_select(self):
        return Select(self.element)

    def clear_value(self):
        for _ in self.get_value():
            self.element.send_keys(Keys.BACKSPACE)

    def get_value(self):
        return self.get_attribute("value")

    def get_attribute(self, name):
        return self.element.get_attribute(name)

    def click_input(self, text):
        es = self.find_elements(Locator("input", By.TAG_NAME))
        for e in es:
            if e.get_attribute("value") == text:
                e.click()

    def send_keys(self, value):
        self.element.send_keys(str(value))

    def find_element(self, locator):
        return HTMLElement(self.element.find_element(value=locator.find_target, by=locator.by))

    def find_elements(self, locator):
        elements = self.element.find_elements(value=locator.find_target, by=locator.by)
        return HTMLElementList([HTMLElement(e) for e in elements])

    def select_set_value(self, value, select_by_value=False):
        sel = Select(self.element)
        if not select_by_value:
            sel.select_by_visible_text(value)
        else:
            sel.select_by_value(value)

    def is_stale(self):
        try:
            self.element.is_enabled()
            return False
        except StaleElementReferenceException:
            return True

    def has_attribute(self, name):
        try:
            self.get_attribute(name)
            return True
        except AttributeError:
            return False

    def click(self):
        self.element.click()

    def submit(self):
        self.element.submit()

    def is_displayed(self):
        return self.element.is_displayed()

    def is_enabled(self):
        return self.element.is_enabled()

    def take_image(self):
        self.element.screenshot(f"/Images/{datetime.now().time().strftime('%M_%S_%f')}.png")