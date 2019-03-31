from collections import namedtuple

from lztools.pytools import import_class

BrowserController = import_class()
GenericPage = import_class()
HTMLElement = import_class()
HTMLElementList = import_class()
LocatorCollection = import_class()
ElementVisibilityTimeout = import_class()
Driver = import_class()

Locator = namedtuple("Locator", ["find_target", "by"])

__all__ = [BrowserController, Driver, GenericPage, HTMLElement, HTMLElementList, LocatorCollection, ElementVisibilityTimeout, Locator]