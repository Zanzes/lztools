class Descriptor(object):
    """A descriptor that does nothing intended for inheritance (Normally used in the DescriptorDict)"""
    value = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __repr__(self):
        return str(self.value)
