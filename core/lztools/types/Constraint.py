from lztools.types.Descriptor import Descriptor

class Constraint(Descriptor):
    constraining_type = None
    type_constraint_enabled = False

    max_length = -1
    length_constraint_enabled = False

    max = -1
    max_num_constraint_enabled = False

    min = -1
    min_num_constraint_enabled = False

    def __init__(self, *args, constraining_type=None, max_length=-1, max_num=-1, min_num=-1, **kwargs):
        if constraining_type is not None:
            self.constraining_type = constraining_type
            self.type_constraint_enabled = True
        if max_length > 0:
            self.max_length = max_length
            self.length_constraint_enabled = True
        if max_num > 0:
            self.max = max_num
            self.max_num_constraint_enabled = True
        if min_num > 0:
            self.min = min_num
            self.min_num_constraint_enabled = True
        super().__init__(*args, **kwargs)

    def __get__(self, instance, owner):
        if self.constraining_type == str:
            self.value = self.value
        return self.value

    def __set__(self, instance, value):
        if self.type_constraint_enabled:
            if not isinstance(self.constraining_type, value):
                raise TypeError(f"value did not pass type check: got '{type(value)}' expected '{self.constraining_type}'")

        if self.length_constraint_enabled:
            ln = len(value)
            if ln > self.max_length:
                raise ValueError(f"value did not pass length check: max '{self.max_length}' got '{ln}'")

        if self.max_num_constraint_enabled:
            if value > self.max:
                raise ValueError(f"value ({value}) is bigger than {self.max}")

        if self.min_num_constraint_enabled:
            if value < self.min:
                raise ValueError(f"value ({value}) is less than {self.min}")

        self.value = value

    def __repr__(self):
        return str(self.value)