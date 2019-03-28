import json
from pathlib import Path


import pickle

resources_path = get_module_path(MiRResources)

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