#!  /usr/bin/env python3.7
from functools import partial
from itertools import groupby
from pprint import pprint
from types import FunctionType

from lztools.Data.Images import get_random_image, search

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def a():
    time_operation(partial(search, "abcd", 1), 800, id="Find")
def b():
    time_operation(get_random_image, 800, id="Rand")

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

    class Item(object):
        prop_a = None
        prop_b = None
        prop_c = None

        def __init__(self, a, b, c):
            self.prop_a = a
            self.prop_b = b
            self.prop_c = c

        def __repr__(self):
            return f"item: a->{self.prop_a} b->{self.prop_b} c->{self.prop_c}"



    items = [
        Item(11, "23", 3.3),
        Item(11, "21", 3.3),
        Item(12, "21", 3.1),
        Item(12, "22", 3.1),
        Item(13, "22", 3.2),
        Item(13, "23", 3.2),
    ]

    #pprint(items)

    for k, v in group_by(items, lambda x: x.prop_a):
        print(f"{k}: {v}")
        for val in v:
            print(f"\t{val}")

    # a = A()
    # print("a created")
    # a.is_wraped()

    # y = subprocess.check_output(["echo", "123"])
    # x = return_command_result("echo", "123\nass")
    # print(x)

    # w = BlockWriter()
    #
    # w.square_text("Joe sucks")
    # w.seperate()
    # w.write_text("tis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjaw\ntis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjawtis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjawtis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjaw")
    # w.seperate()
    # try:
    #     print(2 * "llo" / "a")
    # except Exception as e:
    #     w.split()
    #     w.seperate()
    #     exc_type, exc_value, exc_traceback = sys.exc_info()
    #     t = traceback.format_exception(exc_type, exc_value, exc_traceback)
    #     for x in t:
    #         w.write_text(x, colorizer=Ansi.red)
    #     w.seperate()
    # w.flush()

    # print(create_line(create_line()))
    # print(create_line(create_line(text="asdw=:;")))
    #
    # cm = ColumnWriter()
    # cm.mark_column("lol", "First", "X")
    # cm.mark_column("lol2", "First", "X")
    # cm.mark_column("lol", "Second", "X")
    # print(cm.flush())

    # w = ColumnWriter(width=200)
    # w.add_mark("Joe", "First", "X")
    # w.add_mark("Joe", "Second", "X")
    # w.add_mark("Jack", "Second", "X")
    #
    # print(w.get_header())
    # for row in w.get_rows():
    #     print(row)




