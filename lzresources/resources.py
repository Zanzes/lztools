import json
import pickle
from pathlib import Path

from pathing import get_module_path

import lzresources

resources_path = get_module_path(lzresources)

class ResourceFormat(object):
    pickle = "pickle"
    json = "json"

def item_exists(name):
    if name in [item.name for item in resources_path.iterdir()]:
        return True
    return resources_path.joinpath(name).exists()

def _save_json(item, path: Path):
    if not path.exists():
        path.touch()
    with open(path, "r+b") as file:
        json.dump(item, file)

def _save_pickle(item, path: Path):
    if not path.exists():
        path.touch()
    with open(path, "r+b") as file:
        pickle.dump(item, file)

def save(item, name: str, save_format: ResourceFormat = ResourceFormat.json):
    if save_format == ResourceFormat.json:
        _save_json(item, resources_path.joinpath(f"{name}.json"))
    elif save_format == ResourceFormat.pickle:
        _save_pickle(item, resources_path.joinpath(f"{name}.pkl"))

def _load_pickle(name):
    with open(resources_path.joinpath(name + ".pkl"), "r+b") as file:
        return pickle.load(file)

def _load_json(name):
    with open(resources_path.joinpath(name + ".json"), "r+b") as file:
        return json.load(file)

def load(name, save_format: ResourceFormat = ResourceFormat.json):
    if save_format == ResourceFormat.json:
        return _load_json(name)
    elif save_format == ResourceFormat.pickle:
        return _load_pickle(name)

def find(name) -> Path:
    items = list(resources_path.glob(f"{name}.*"))
    return items[0]


# class ConfigManager(object):
#     _managers = {}
#     _manager = None
#     _original = None
#
#     @staticmethod
#     def get_manager(name):
#         return ConfigManager._managers[name]
#
#     @staticmethod
#     def add_manager(name, manager):
#         ConfigManager._managers[name] = manager
#
#     @classmethod
#     def create_manager(cls, name, config_file, config_type=None, save_overrides=False):
#         with TempPath(MiRResources.__path__._path[0]):
#             if not os.path.exists(config_file):
#                 raise Exception(f"Currently in directory: {os.getcwd()}\nFile not found: {config_file}")
#             if config_type is not None:
#                 _type = config_type
#             elif config_file.endswith(".ini"):
#                 _type = ConfigType.ini
#             elif config_file.endswith(".json"):
#                 _type = ConfigType.json
#             else:
#                 raise Exception("Config type not recognised")
#
#             if _type == ConfigType.ini:
#                 cls._managers[name] = IniConfig(config_file, save_overrides)
#             if _type == ConfigType.json:
#                 cls._managers[name] = JsonConfig(config_file, save_overrides)
#         return ConfigManager._managers[name]
#
#     @staticmethod
#     def load_config(path, config_type=None):
#         with TempPath(MiRResources.__file__):
#             if not os.path.exists(path):
#                 raise Exception(f"Currently in directory: {os.getcwd()}\nFile not found: {path}")
#             if config_type is not None:
#                 _type = config_type
#             elif path.endswith(".ini"):
#                 _type = ConfigType.ini
#             elif path.endswith(".json"):
#                 _type = ConfigType.json
#             else:
#                 raise Exception("Config type not recognised")
#             res = None
#             if _type == ConfigType.ini:
#                 p = ConfigParser()
#                 p.read(path)
#                 res = p.sections()
#             elif _type == ConfigType.json:
#                 with open(path) as f:
#                     res = json.load(f)
#         return res
#
#     def __class_getitem__(cls, item):
#         if item not in ConfigManager._managers:
#             items = list(Path(get_module_path(MiRResources)).glob(f"{item}.*"))
#
#             if len(items) != 1:
#                 raise FileNotFoundError(f"Resource not found in resources: {item}")
#             f = str(items[0])
#             if not f.endswith("json") and not f.endswith("ini"):
#                 raise FileNotFoundError(f"Resource not found in resources: {item}")
#             ConfigManager.create_manager(item, f)
#         return ConfigManager.get_manager(item)
#
# class IniConfig(dict):
#     path = None
#     temp_values = None
#     save_overrides = None
#     parser = None
#     default_section = "default_section"
#
#     def __init__(self, config_file, save_overrides=False):
#         self.path = config_file
#         self.save_overrides = save_overrides
#         self.temp_values = {}
#         self.parser = ConfigParser()
#         self.parser.read(config_file)
#         super().__init__(self.parser._sections)
#
#     def __getattribute__(self, item):
#         v = None
#         if item in IniConfig.__dict__:
#             return object.__getattribute__(self, item)
#         if item in self.temp_values:
#             v = self.temp_values[item]
#         elif self.option_exists(item):
#             for s in self.parser.sections():
#                 if self.parser.has_option(s, item):
#                     v = self.parser.get(s, item)
#                     break
#         else:
#             return object.__getattribute__(self, item)
#         return v
#
#     def set_option(self, option, value):
#         for sect in self.parser.sections():
#             if self.parser.has_option(sect, option):
#                 self.parser.set(sect, option, value)
#                 break
#
#     def __setattr__(self, key, value):
#         if key in IniConfig.__dict__:
#             object.__setattr__(self, key, value)
#             return
#         if self.save_overrides:
#             if self.option_exists(key):
#                 self.set_option(key, value)
#             else:
#                 self.parser.set(self.default_section, key, value)
#         else:
#             self.temp_values[key] = value
#
#     def option_exists(self, name):
#         for sect in self.parser.sections():
#             if self.parser.has_option(sect, name):
#                 return True
#         return False
#
# class JsonConfig(dict):
#     path = None
#     temp_values:dict = None
#     save_overrides = None
#
#     def __init__(self, config_file, save_overrides=False):
#         self.path = config_file
#         self.save_overrides = save_overrides
#         self.temp_values = {}
#         with open(config_file, "r+") as f:
#             super().__init__(json.load(f))
#
#     def __getattribute__(self, item):
#         if item in JsonConfig.__dict__:
#             return object.__getattribute__(self, item)
#         val = None
#         if item in self.temp_values:
#             val = self.temp_values[item]
#         elif item in self:
#             val = self[item]
#         if val is not None:
#             return val
#         return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key in JsonConfig.__dict__:
#             return object.__setattr__(self, key, value)
#         if self.save_overrides:
#             self[key] = value
#         else:
#             self.temp_values[key] = value
#
#     def __iter__(self):
#         for k, v in self.iteritems():
#             yield k, v
#
# def get_site_path(name):
#     return get_module_path(MiRResources).joinpath(f"{name}.site")
#
# def extract_site(path:Path, password, delete_site_file=False):
#     d:Path = path.parent
#     sh.gpg("--no-tty", "--batch", "--passphrase", password, "-d", path, _out=str(d.joinpath("zip.zip")))
#     call(["python", "-m", "zipfile", "-e", str(d.joinpath("zip.zip")), str(d)])
#     call(["rm", "-rf", str(d.joinpath("zip.zip"))])
#     if delete_site_file:
#         call(["rm", "-rf", str(path)])
#     with open(d.joinpath("session.json")) as f:
#         return AutoInitialized(json.load(f))