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
