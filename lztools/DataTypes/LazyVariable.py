import inspect
import gc
import pprint
import types
from types import ModuleType

import sys

from lztools.Data.flickr import joe

joe()

class Descriptor(object):
    def __get__(self, instance, owner):
        print("get")

    def __set__(self, instance, value):
        print("set")

class LazyVariable(object):
    def __init__(self, load):
        types.ModuleType
        print(__name__)

    def find_names(self):
        frame = inspect.currentframe()
        for frame in iter(lambda: frame.f_back, None):
            frame.f_locals
        obj_names = []
        for referrer in gc.get_referrers(self):
            if isinstance(referrer, dict):
                for k, v in referrer.items():
                    if v is self:
                        obj_names.append(k)
        pprint.pprint(obj_names)


class VerboseModule(ModuleType):
    def __repr__(self):
        print(f'Verbose {self.__name__}')
        return f'Verbose {self.__name__}'

    def __setattr__(self, attr, value):
        print(f'Setting {attr}...')
        setattr(self, attr, value)
def do():
    sys.modules[__name__].__class__ = VerboseModule