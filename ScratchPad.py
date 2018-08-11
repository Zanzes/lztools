#!  /usr/bin/env python3.7
from functools import partial
from itertools import groupby
from pprint import pprint
from types import FunctionType

from lztools.Data.Images import get_random_image, search

def pi(imgs):
    for img in imgs:
        print(img)

def dec1(func:FunctionType):
    print(f"wrapping: {func.__name__}")
    def lolfunc(self):
        print("lol now")
        func(self)
    return lolfunc

class A(object):

    @dec1
    def is_wraped(self):
        print("Final")

_og = groupby

def group_by(iter, key_func):
    data = sorted(iter, key=key_func)
    return _og(data, key_func)

if __name__ == '__main__':

    a = A()
    print("a created")
    a.is_wraped()




