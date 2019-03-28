#!  /usr/bin/env python
# -*- coding: utf-8 -*-
import inspect, sys
from functools import wraps

from ui_framework.generator import User

def assert_log(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        l = list(args)
        for kw in kwargs:
            l.append(kwargs[kw])
        text = f"{func.__name__}({', '.join([str(arg) for arg in args])})"
        inspect.stack()[1][0].f_globals["meta"]["asserts"].append(text)
        return func(*args, **kwargs)
    return function_wrapper

def get_api():
    from ui_framework import runner
    return runner.active_run.api

@assert_log
def is_true(expr):
    if expr is not True:
        _throw(f"x != True => ({expr} != True)")

@assert_log
def is_false(expr):
    if expr is not False:
        _throw(f"x != False => ({expr} != False)")

@assert_log
def is_not_none(expr):
    if expr is None:
        _throw(f"x == None => ({expr} == None)")

@assert_log
def is_not_empty(list):
    if len(list) <= 0:
        _throw(f"x is empty => ({list} == [])")

@assert_log
def is_none(expr):
    if expr is not None:
        _throw(f"x != None => ({expr} != None)")

@assert_log
def equal(left, right):
    if not left == right:
        _throw(f"x == y x does not equal y => ({left} == {right})")

@assert_log
def is_not_equal(left, right):
    if left == right:
        _throw(f"x != y x equals y => ({left} != {right})")

@assert_log
def is_greater_than(left, right):
    if not left > right:
        _throw(f"x > y x is not greater than y => ({left} > {right})")

@assert_log
def is_less_than(left, right):
    if not left < right:
        _throw(f"x < y x is not less than y => ({left} < {right})")

@assert_log
def fail():
    _throw("Assert.fail() called!")

@assert_log
def throws(func, exception_type):
    try:
        func()
    except exception_type:
        return
    except Exception as e:
        _throw(f"Expected exception of type: {exception_type}\nGot: {e}")

def _throw(text):
    raise AssertionError(f"{text}")

@assert_log
def user_exists(user:User):
    users = get_api().users.all().details()
    lis = [u for u in users if u.name == user.name and u.username == user.username]
    assert len(lis) == 1

@assert_log
def site_exists(site_name):
    assert site_name in [session.name for session in get_api().sessions.all()]

@assert_log
def map_exists(map):
    assert map in [map.name for map in get_api().maps.all()]

@assert_log
def dashboard_exists(name):
    assert name in [dash.name for dash in get_api().dashboards.all()]