from pathlib import Path

from lztools.settings import GlobalSettings

_storage_folder = ".lztools"

settings:GlobalSettings = GlobalSettings()

def storage_location() -> Path:
    p = Path.home().joinpath(_storage_folder)
    if not p.exists():
        p.mkdir()
    return p