import atexit
import os
import pickle
import shutil
import tempfile
from contextlib import contextmanager
from datetime import timedelta, datetime
from distutils.errors import DistutilsFileError
from pathlib import Path
from types import FunctionType
from typing import Callable, Any
from lztools import lzglobal
from lztools.enums import FileExtension

_expire_dir = lzglobal.storage_location().joinpath("expires")
_expire_dir.mkdir(exist_ok=True, parents=True)

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

def is_empty(path:Path):
    if path.is_file():
        return path.stat().st_size == 0
    elif path.is_dir():
        for _ in path.iterdir():
            return False
        return True
    else:
        raise Exception(f"""Unhandled case! path:{type(path)} -> {path}""")

def get_temporary_file() -> Path:
    """Creates a temporary file withc is automatically deleted when the program exits"""
    tmp_file = Path(tempfile.mkstemp()[1])
    tmp_file.touch()
    atexit.register(lambda: tmp_file.unlink())
    return tmp_file

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

def _gen_exp_fn(name):
    return f"{name}¤{datetime.now()}.{FileExtension.expiring_file}"

def get_expiring_file(name:str, expires_after:timedelta) -> Path:
    for file in _expire_dir.glob(f"{name}¤*.{FileExtension.expiring_file}"):
        f_name, f_date = file.name.split("¤")
        f_date = datetime.fromisoformat(f_date.split(f".{FileExtension.expiring_file}")[0])
        delta = datetime.now() - f_date
        if delta > expires_after:
            file.unlink()
            file = file.with_name(_gen_exp_fn(name))
        file.touch(exist_ok=True)
        return file
    file = _expire_dir.joinpath(_gen_exp_fn(name))
    file.touch()
    return file

def get_self_renewing_file(name:str, renew_after:timedelta, renew:FunctionType, pickle_data=True) -> Path:
    file = get_expiring_file(name, expires_after=renew_after)
    if is_empty(file):
        data = renew()
        if pickle_data:
            with file.open("wb") as f:
                pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        else:
            file.write_text(data)
        return data
    with file.open("rb") as f:
        return pickle.load(f)





