import os
import shutil

from contextlib import contextmanager
from distutils.errors import DistutilsFileError
from pathlib import Path
from typing import Callable, Any

import errno

def get_current_path() -> Path:
    return Path(".").absolute()

def get_current_path_str() -> str:
    return str(get_current_path())

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
from distutils.dir_util import copy_tree

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

def copy_directory(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def copy_anything(src, dst):
    try:
        #copy_directory(src, dst)
        copy_tree(str(src), str(dst))
    except DistutilsFileError as exc:
        shutil.copy(src, dst)

def scatter_files(base_path:Path, recursive:bool=True, scatter_name:str="_scatter_", sudo:bool=False):
    if not base_path:
        base_path = get_current_path()

    for item in base_path.iterdir():
        if item.name == scatter_name:
            _scatter_file_routine(item, sudo)
        if recursive and item.is_dir():
            scatter_files(item, recursive)

def _scatter_file_routine(scatter_file:Path, sudo:bool=False):
    text = scatter_file.read_text()
    for line in text.strip().splitlines():
        if "->" not in line:
            continue
        if line.startswith("#"):
            continue
        split = line.split("->")
        if not len(split) == 2:
            continue
        path_a:Path = scatter_file.parent.joinpath(split[0].strip())
        path_b = Path(split[1].strip()).expanduser()

        from lztools import lzglobal
        if lzglobal.settings.verbose:
            print(f"Copying: {path_a.absolute()} -> {path_b.absolute()}")
        if not sudo:
            copy_anything(path_a, path_b)
        else:
            os.system(f"sudo cp {path_a.absolute()} {path_b.absolute()}")
