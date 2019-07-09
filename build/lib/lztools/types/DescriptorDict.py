from abc import ABC
from collections import defaultdict

from lztools.types.Descriptor import Descriptor

class DescriptorDict(ABC):
    """A dictionary in witch descriptors (inheriting from Descriptor) are enabled"""
    backing = None

    def __init__(self, backer:dict=None):
        if backer is None:
            self.backing = defaultdict()
        else:
            object.__setattr__(self, "backing", backer.copy())

    def __getattribute__(self, item):
        try:
            ob = object.__getattribute__(self, "backing")[item]
            if isinstance(ob, Descriptor):
                return ob.__get__(self, self)
            return ob
        except:
            return object.__getattribute__(self, item)

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __setattr__(self, key, value):
        backing = object.__getattribute__(self, "backing")
        if key not in backing:
            backing[key] = value
        else:
            if isinstance(backing[key], Descriptor):
                backing[key].__set__(backing[key], value)
            else:
                object.__getattribute__(self, "backing")[key] = value

    def items(self):
        for key in object.__getattribute__(self, "backing"):
            yield key, object.__getattribute__(self, "backing")[key]

    def update(self, values:dict):
        for key, value in values.items():
            self[key] = value

DescriptorDict.register(dict)
