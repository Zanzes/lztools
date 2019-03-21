from collections import defaultdict

class Descriptor(object):
    value = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class Constraint(Descriptor):
    constraining_type = None

    def __init__(self, *args, type, default=None, **kwargs):
        self.constraining_type = type
        self.value = default
        super().__init__(*args, **kwargs)

    def __get__(self, instance, owner):
        if self.constraining_type == str:
            self.value = self.value
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, self.constraining_type):
            raise TypeError(f"The set value is not an instance of {self.constraining_type} rather {type(value)}")
        self.value = value

    def __repr__(self):
        return str(self.value)

class HttpString(Descriptor):
    value = None

    def _fixup(self):
        if not self.value.startswith("http"):  # and self.value != "localhost":
            self.value = f"http://{self.value}"

    def __init__(self, *args, default="", **kwargs):
        if default is None:
            default = ""
        self.value = default
        super().__init__(*args, **kwargs)

    def __get__(self, instance, owner):
        self._fixup()
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"The value is not an instance of {str} rather {type(value)}")
        self.value = value

    def __repr__(self):
        self._fixup()
        return self.value

class DescriptorDict(object):
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