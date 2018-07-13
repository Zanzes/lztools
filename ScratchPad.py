#!  /usr/bin/env python
import asyncio
from functools import partial
from multiprocessing import Process
from multiprocessing.pool import Pool

from lztools.Data.Images import get_random_image, search
from lztools.Debugging import time_operation

def a():
    time_operation(partial(search, "abcd", 1), 800, id="Find")
def b():
    time_operation(get_random_image, 800, id="Rand")

p1 = Process(target=a)
p2 = Process(target=b)
p1.start()
p2.start()
p1.join()
p2.join()