import importlib
import inspect

import sys

def import_class():
    callers_local_vars = inspect.currentframe().f_back
    nr = callers_local_vars.f_lineno - 1
    line = inspect.getsource(callers_local_vars).splitlines()[nr]
    name = line.split("=")[0].split(":")[0].strip()
    module = importlib.import_module("."+name, inspect.getmodule(callers_local_vars).__package__)
    cls = getattr(module, name)
    sys.modules[name] = cls
    return cls