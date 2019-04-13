import inspect
from types import FunctionType

def get_method_names(klass):
    return [method[0] for method in inspect.getmembers(klass) if not method[0].startswith("_") and (type(method[1]) == FunctionType and method[1].__module__ == klass.__name__)]

def get_methods(klass):
    return [method for method in inspect.getmembers(klass) if not method[0].startswith("_")]