import os

from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Any

def get_current_path():
    return str(Path(".").absolute())

def is_escaped(text, index) -> bool:
    def __is_escaped(t, i, v) -> bool:
        if t[i-1] == "\\":
            return __is_escaped(t, i-1, not v)
        else:
            return v
    return __is_escaped(text, index, False)

def name_and_ext(path) -> str:
    rsplit = str(path).rsplit("/", 1)
    return rsplit[1] if len(rsplit) > 1 else path

def remove_extension(path) -> str:
    return str(path).rsplit(".", 1)[0]

def name(path) -> str:
    return remove_extension(name_and_ext(path))

# def get_module_path(target, return_string=False) -> Union[Path, str]:
#     mp = None
#     if hasattr(target, "__path__") and target.__path__:
#         mp = next(iter(target.__path__))
#     elif hasattr(target, "__file__") and target.__file__:
#         mp = target.__file__
#     elif hasattr(target, "__module__") and target.__module__:
#         mp = get_module_path(sys.modules[target.__module__])
#     else:
#         try:
#             mp = inspect.getsourcefile(target)
#         except:
#             pass
#     if not mp:
#         raise Exception(f"Cant find path to target (type: {type(target)}, value: {target})")
#     if return_string:
#         return mp
#     return Path(mp)

def move_to(path, relative=True):
    if relative:
        path = os.path.realpath(path)
    if os.path.isfile(path):
        path = os.path.dirname(path)
    original = os.getcwd()

    os.chdir(path)

    def move_back():
        os.chdir(original)
    return move_back

@contextmanager
def TempPath(path):
    move_back = move_to(path)
    yield
    move_back()

def on_all(action:Callable[[Path], Any], path:Path, subdirs:bool=True):
    for p in path.absolute().iterdir():
        if p.is_dir() and subdirs:
            yield from on_all(action, p)
        yield action(p)

def on_files(on_files:Callable[[Path], Any], path:Path, subdirs:bool=True):
    def do(p:Path):
        if p.is_file():
            return on_files(p)
    for result in on_all(do, path, subdirs):
        if result is not None:
            yield result

def on_dirs(on_dirs:Callable[[Path], Any], path:Path, subdirs:bool=True):
    def do(p:Path):
        if p.is_dir():
            return on_dirs(p)
    for result in on_all(do, path, subdirs):
        if result is not None:
            yield result

# class TempPath(object):
#     original_path = None
#     new_path = None
#
#     def __init__(self, path):
#         self.original_path = os.getcwd()
#         self.new_path = os.path.realpath(path)
#
#     def __enter__(self):
#         os.chdir(self.new_path)
#         return self.new_path
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         os.chdir(self.original_path)