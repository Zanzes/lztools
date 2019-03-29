import json
import pickle
from pathlib import Path
from subprocess import call

from git import clone_repo, repos
from lztools.lzconstants import data_loader_bash_script

from mod_tools import get_module_path

import lzresources
from pathing import TempPath

_user_home = Path.home().absolute()
main_path = _user_home .joinpath(".lztools").absolute()
scripts_path = main_path.joinpath("scripts")
loader_path = scripts_path.joinpath("data_loader")
data_path = main_path.joinpath("data")
out_path = data_path.joinpath("out_data")
resources_path = main_path.joinpath("lzresources")
bashrc_path = _user_home.joinpath(".bashrc")

def ensure_initialized(override=False):
    if override:
        call(["rm", "-rf", str(main_path)])
    if not main_path.exists():
        main_path.mkdir()
        scripts_path.mkdir()
        loader_path.touch()
        data_path.mkdir()
        out_path.touch()
        loader_path.write_text(data_loader_bash_script.format(out_path.absolute()))

        with TempPath(main_path.absolute()):
            clone_repo(repos.Resources)

        data = bashrc_path.read_text()
        if "PROMPT_COMMAND" not in data:
            marker = "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> OTHER END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙"
            data = data.replace(f"\n\n{marker}", f"\nPROMPT_COMMAND='source {str(loader_path)}'\n\n{marker}")
            bashrc_path.write_text(data)

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