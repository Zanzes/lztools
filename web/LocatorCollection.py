from web.web import Locator

class LocatorCollection(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, Locator) and (isinstance(value, tuple) or isinstance(value, list)):
            value = Locator(value[0], value[1])
        super(LocatorCollection, self).__setitem__(key, value)
