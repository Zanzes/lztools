class Flag(object):
    value = None

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    @staticmethod
    def has_flag(val, flag):
        return (val | flag) > 0