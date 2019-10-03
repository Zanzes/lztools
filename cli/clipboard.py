import click

from lztools import bash
from lztools import zlick


@zlick.command_matching_group()
def main():
    """A collection of convenient bash tools"""

@main.command(name="print")
@click.option("-b", "--buffer", type=click.Choice(['primary', 'secondary', 'clipboard']),
                default='primary', show_default=True, help="Selects witch buffer to output")
def output(buffer):
    print(bash.get_clipboard_content(buffer))