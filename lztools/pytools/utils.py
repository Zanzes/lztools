import inspect
import sys
from importlib import import_module
from inspect import currentframe, getsource, getmodule

def get_variable_type_hint(variable):
    from lztools import lztext
    cf = inspect.currentframe()
    f = cf.f_back
    filename = inspect.getfile(f)
    code_line = open(filename).readlines()[f.f_lineno - 1]
    t = f"{get_variable_type_hint.__name__}("
    i = code_line.find(t) + len(t)
    e = lztext.find_matching(lztext.matching.parentheses, code_line, offset=i)
    name = code_line[i:e]
    if "." in name:
        a, name = name.split(".", 1)
        mod = eval(a, f.f_globals)
        if "." in name:
            while "." in name:
                a, name = name.split(".", 1)
                mod = getattr(mod, a)
        annotations = mod.__annotations__
    else:

        val = eval(name, f.f_globals)
        mod = inspect.getmodule(val)
        annotations = mod.__annotations__ if mod else {}
    r = annotations.get(name, None)
    return r if r else f.f_globals["__annotations__"].get(name, None)

def import_class():
    frame = currentframe().f_back
    line = getsource(frame).splitlines()[frame.f_lineno - 1]
    name = line.split("=")[0].split(":")[0].strip()
    module = import_module("."+name, getmodule(frame).__package__)
    cls = getattr(module, name)
    sys.modules[name] = cls
    return cls