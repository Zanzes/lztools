from pprint import pprint

class Magic(object):

    class A(object):
        pass
    get = None

    def __init__(self, x):
        self.get = x

    def __get__(self, instance, owner):
        print(f"Getting {instance} {owner}")
        return self.get

class B(object):
    m = Magic(321)

class Holder(object):
    m4:123 = None
    pass

h = Holder()

m3:str = "asd"
m2:B = Magic.A()
m1:Magic.A = Magic(123)

# pprint(locals())
# exit()