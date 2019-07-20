from __future__ import annotations

from pathlib import Path


class SettingsGroup(object):

    @classmethod
    def create(cls, **kwargs):
        self = cls()
        self.__dict__.update(kwargs)
        return self

    def set(self, **kwargs):
        self.__dict__.update(kwargs)

class GlobalSettings(SettingsGroup):
    verbose = False
    working_dir:Path = None
    quiet = False

    def __init__(self):
        from lztools import io
        self.working_dir = io.get_current_path()

