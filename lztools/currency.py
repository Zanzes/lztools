import datetime
import os, json, pickle

from lztools import bash
import requests

from lztools.lzglobal import storage_location

rates = []
base = None

def update_rates():
    json:dict = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={os.environ['OERID']}").json()
    # rates = json['rates']
    # base = json['base']
    p = storage_location().joinpath(f"{datetime.datetime.now()}_{json['base']}_.rates")
    if p.exists():
        p.unlink()
    p.touch()
    with p.open("wb") as f:
        pickle.dump(json['rates'], f, pickle.HIGHEST_PROTOCOL)

def get_rates():
    update_rates()
    global base, rates
    has_files = False
    for file in storage_location().glob("*.rates"):
        date, base, _ = file.name.split("_")
        has_files = True
        with file.open("rb") as f:
            rates = pickle.load(f)
    print("d1")

def print_rates(currencies:list):
    for rate in rates:
        if not currencies:
            print(f"{rate}: {rates[rate]}")
        elif rate in currencies:
            print(f"{rate}: {rates[rate]}")

def _to_base(value, abrv:str):
    return value / rates[abrv.upper()]

def _from_base(value, abrv:str):
    return rates[abrv.upper()] * value

def convert(value, from_abrv:str, to_abrv:str):
    return _from_base(_to_base(value, from_abrv), to_abrv)

