from __future__ import annotations

import random
from string import digits
from typing import List

generated_users:List[User] = []
generated_ints = []

def generate_int(digit_count=5) -> int:
    i = int("".join([random.choice(digits) for _ in range(digit_count)]))
    generated_ints.append(i)
    return i

def generate_ints(count, digit_count=5) -> List[int]:
    return [generate_int(digit_count) for _ in range(count)]

def last_generate_int(count:int=1):
    if count == 1:
        return generated_ints[-1]
    return [generated_ints[-i] for i in range(1, count + 1)]

def generate_text(length, safe=False):
    from MiR.text import generate_text
    return generate_text(length, safe)

class User(object):
    name: str
    username: str
    password: str
    email: str
    group: str
    pin: int
    using_pin: bool
    single_dashboard: bool

    def __init__(self, name: str = None, username: str = None, password: str = None, email: str = None, group: str = None, pin: int = None, using_pin: bool = False, single_dsahboard: bool = False):
        self.name = name if name else generate_text(40)
        self.username = username if username else generate_text(40)
        self.password = password if password else generate_text(40)
        self.email = email if email else f"{generate_text(30, safe=True)}@{generate_text(5, safe=True)}.com"
        self.group = group if group else generate_text(40)
        self.pin = pin if pin else generate_int(4)
        self.using_pin = using_pin
        self.single_dashboard = single_dsahboard

def last_generated_user(count:int=1):
    if count == 1:
        return generated_users[-1]
    return [generated_users[-i] for i in range(1, count + 1)]

def generate_user(name: str = None, username: str = None, password: str = None, email: str = None, group: str = None, pin: int = None, using_pin: bool = False, single_dsahboard: bool = False) -> User:
    generated_users.append(User(name, username, password, email, group, pin, using_pin, single_dsahboard))
    return last_generated_user()

def generate_users(count):
    return [generate_user() for _ in range(count)]