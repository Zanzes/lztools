import os

class A(object):
    y = "success"

    def __getitem__(self, item):
        if item == "x":
            return self.y
        return super(A, self).__getitem__(item)

a = A()

print(a["x"])