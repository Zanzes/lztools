#!  /usr/bin/env python
from functools import partial

from lztools.BlockWriter import BlockWriter
from lztools.debugging import time_operation

from lztools.Data.Images import get_random_image, search
from lztools.text import box_text, wall_text

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def a():
    time_operation(partial(search, "abcd", 1), 800, id="Find")
def b():
    time_operation(get_random_image, 800, id="Rand")

def pi(imgs):
    for img in imgs:
        print(img)

if __name__ == '__main__':
    # y = subprocess.check_output(["echo", "123"])
    # x = return_command_result("echo", "123\nass")
    # print(x)
    w = BlockWriter()

    w.square_text("Joe sucks")
    w.seperate()
    w.write_text("tis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjaw\ntis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjawtis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjawtis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjaw")
    w.seperate()
    w.flush()
    print("")
    print(wall_text("joe is a dick", width=20))





