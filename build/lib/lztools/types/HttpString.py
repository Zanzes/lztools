from lztools.types.Descriptor import Descriptor

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