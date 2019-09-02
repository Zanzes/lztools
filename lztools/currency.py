import os, json

from lztools import bash
import requests
rates = []
base = None

def update_rates():
    global base, rates
    json:dict = requests.get(f"https://openexchangerates.org/api/latest.json?app_id={os.environ['OERID']}").json()
    rates = json['rates']
    base = json['base']

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

