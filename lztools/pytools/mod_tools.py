import inspect
import os
import sys
from pathlib import Path
from types import GeneratorType, ModuleType

def import_files(path:Path, package, includes:dict=None) -> GeneratorType:
    for file in path.iterdir():
        if not file.name.endswith(".py"):
            continue
        yield import_file(file, package, includes)

def import_file(file:Path, package, includes:dict=None) -> ModuleType:
    text = file.read_text()
    name = file.name[:-3]
    if os.pathsep in name:
        name = name.rsplit(os.pathsep, 1)[1]
    mod = ModuleType(name)
    if includes:
        includes = includes.copy()
        mod.__dict__.update(includes)
    mod.__file__ = str(file.absolute())
    mod.__package__ = package
    code = compile(text, mod.__file__, 'exec')
    exec(code, mod.__dict__)
    return mod

def get_module_path(target):
    if hasattr(target, "__path__") and target.__path__:
        return next(iter(target.__path__))
    elif hasattr(target, "__file__") and target.__file__:
        return target.__file__
    elif hasattr(target, "__module__") and target.__module__:
        return get_module_path(sys.modules[target.__module__])
    try:
        return inspect.getsourcefile(target)
    except:
        pass
    raise Exception(f"Cant find path to target (type: {type(target)}, value: {target})")

def ignore_exception(func, exception, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except exception:
        pass