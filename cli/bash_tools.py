import os

import click

from lztools import zlick, bash, currency


@zlick.command_matching_group()
def main():
    """A collection of convenient bash tools"""

@main.group(cls=zlick.CommandMatchingGroup)
def clipboard():
    pass

@clipboard.command(name="print")
@click.option("-b", "--buffer", type=click.Choice(['primary', 'secondary', 'clipboard']),
                default='primary', show_default=True, help="Selects witch buffer to output")
def output(buffer):
    print(bash.get_clipboard_content(buffer))

@main.command()
@click.argument("VALUE", type=click.FLOAT)
@click.argument("FROM_A")
@click.argument("TO_B")
def convert(value, from_a, to_b):
    currency.update_rates()
    print(currency.convert(value, from_a, to_b))

@main.command()
@click.option("-c", "--currencies", multiple=True)
@click.option("-s", "--skip-update", is_flag=True, help="Do not update to the current exchange-rate and print old rate")
def pp(currencies, skip_update):
    if not skip_update:
        currency.update_rates()
    currency.print_rates(currencies)