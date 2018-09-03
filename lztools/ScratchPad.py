from typing import List

import scratch
from lztools.debugging import is_debugging
from lztools.extensions import get_variable_type_hint
from lztools.text import as_literal

class PriorityItem(object):
    priority = None
    value = None

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

class HighPriorityQueue(object):
    items:List[PriorityItem] = []

    def push(self, item, priority):
        i = 0
        for k, v in enumerate(reversed(self.items)):
            if v.priority < priority:
                self.items.insert(k, (PriorityItem(item, priority)))
                return
        self.items.insert(0, (PriorityItem(item, priority)))

    def __iter__(self):
        return iter(sorted(self.items, key=lambda x: x.priority))

    def pop(self):
        return self.items.pop(0)

queue = HighPriorityQueue()

queue.push("asd1", 1)
queue.push("asd2", 3)
queue.push("asd3x", 2)
queue.push("asd3", 2)

for x in queue:
    print(f"{x.priority}: {x.value}")
print("")
queue.pop()
queue.pop()
for x in queue:
    print(f"{x.priority}: {x.value}")