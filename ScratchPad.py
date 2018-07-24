#!  /usr/bin/env python
import subprocess
from functools import partial

from lztools.Bash import return_command_result
from lztools.Data.Images import get_random_image, search
from lztools.Debugging import time_operation
from lztools.text import box

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
    box("lol")





