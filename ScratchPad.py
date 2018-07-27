#!  /usr/bin/env python
import sys
import traceback
from functools import partial

from lztools import Ansi
from lztools.BlockWriter import BlockWriter
from lztools.Data.Images import get_random_image, search
from lztools.debugging import time_operation

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
    try:
        print(2 * "llo" / "a")
    except Exception as e:
        w.split()
        w.seperate()
        exc_type, exc_value, exc_traceback = sys.exc_info()
        t = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for x in t:
            w.write_text(x, colorizer=Ansi.red)
        w.seperate()
    w.flush()




