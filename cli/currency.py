import click
from lztools import zlick, currency

pp = print

@zlick.command_matching_group()
def main():
    pass

@main.command()
@click.argument("VALUE", type=click.FLOAT)
@click.argument("FROM_A")
@click.argument("TO_B")
def convert(value, from_a, to_b):
    currency.get_rates()
    pp(currency.convert(value, from_a, to_b))

@main.command()
def t():
    currency.get_rates()

@main.command()
@click.argument("CURRENCIES", nargs=-1)
def print(currencies):
    if currencies:
        big = []
        for c in currencies:
            big.append(c.upper())
        currencies = big
    currency.get_rates()
    currency.print_rates(currencies)