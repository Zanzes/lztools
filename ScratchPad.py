#!  /usr/bin/env python
from functools import partial
from multiprocessing import Process

import click

from lztools.Data.Images import get_random_image, search
from lztools.Debugging import time_operation

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def a():
    time_operation(partial(search, "abcd", 1), 800, id="Find")
def b():
    time_operation(get_random_image, 800, id="Rand")

def pi(imgs):
    for img in imgs:
        print(img)

if __name__ == '__main__':
    pa = Process(target=a)
    pb = Process(target=b)
    pa.start()
    pb.start()
    pa.join()
    pb.join()
    # pi(get_random_image())
    # pi(get_random_image())
    # pi(get_random_image())
    # pi(get_random_image())
    # pi(get_random_image())
    # pi(get_random_image())
    # pi(get_random_image())
    # pi(get_random_image())
    # pi(get_random_image())
    # pi(get_random_image())
    # pi(get_random_image())
    # pi(get_random_image())
    # print("")
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))
    # pi(get_random_image(count=100))





