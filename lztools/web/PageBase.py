#!  /usr/bin/env python
# -*- coding: utf-8 -*-

from .BrowserController import BrowserController
from .LocatorCollection import LocatorCollection

locators = LocatorCollection()

class PageBase(BrowserController):
    url = None

    def __init__(self, url, skip=False):
        self.url = url
        self.timeout = 10
        super(PageBase, self).__init__()
        if skip:
            return
        self.navigate()

    def navigate(self):
        if self.url != self.get_current_url():
            self.get(self.url)




