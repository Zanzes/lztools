
class EnumMeta(type):
    def __init__(cls, name, bases, clsdict):
        if len(cls.mro()) > 2:
            cls._values = [cls.__getattribute__(cls, val) for val in cls.__dict__ if not val.startswith("_")]

    def __contains__(cls, item):
        # if item in cls.__dict__:
        #     return True
        if item in cls._values:
            return True

class Enum(object, metaclass=EnumMeta):
    _values = None

    @classmethod
    def all(cls):
        for e in cls.__dict__:
            if not e.startswith("_"):
                yield cls.__getattribute__(cls, e)

    @classmethod
    def has_key(cls, key):
        return key in cls.__dict__

    @classmethod
    def has_value(cls, value):
        return value in cls._values

class Flag(object):
    value = None

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    @staticmethod
    def has_flag(val, flag):
        return (val | flag) > 0