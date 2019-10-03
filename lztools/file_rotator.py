from pathlib import Path
from subprocess import call
from typing import Union

def touch(name:str, path:Path, file_count:int=10, open_file:bool=False, extension:str= "mrd"):
    _rotate_forward(path.joinpath(name), extension, file_count)
    p = path.joinpath(name + f"1.{extension}")
    p.touch()
    if open_file:
        return p.open("w")

def _rotate_forward(base_path:Union[str, Path], ext, file_count:int):
    last = Path(f"{base_path}{file_count}.{ext}").absolute()
    if last.exists():
        last.unlink()
    for n in reversed(range(1, file_count + 1)):
        p = Path(f"{base_path}{n}.{ext}")
        if p.exists():
            p.rename(f"{base_path}{n+1}.{ext}")

def add_file(name:str, file:Path, path:Path, extension:str, file_count=10, remove_original=True):
    _rotate_forward(path.joinpath(name), extension, file_count)
    if remove_original:
        file.rename(path.joinpath(name+"1."+extension))
    else:
        call(["cp", str(file.absolute()), str(path.joinpath(name+"1."+extension))])
