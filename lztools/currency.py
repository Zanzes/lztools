import os
import pickle
from datetime import timedelta

import requests

from lztools import lzglobal, io

rates = None
base = None

# RateResult = namedtuple("RateResult", [""])

def get_rates():
    global rates, base
    json = io.get_self_renewing_file("rates", timedelta(minutes=20), lambda: requests.get(f"https://openexchangerates.org/api/latest.json?app_id={os.environ['OERID']}").json())
    rates, base = json['rates'], json['base']

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

