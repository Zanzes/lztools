import click
import re

from lztools import zlick
from lztools import pytools

@zlick.command_matching_group()
def main():
    """Tools to make python development more convenient"""

@main.command()
def clean_build_files():
    """Removes temporary files leftover after build"""
    pytools.cleanup_build_files()

@main.command()
@click.argument("PATH", type=click.Path(exists=True, file_okay=False))
def install_module(path):
    """Installs a python module"""
    pytools.local_install(path)

@main.command()
@click.argument("EXPRESSION", type=click.STRING)
@click.argument("TEXT", type=click.STRING, required=False)
def regex(expression, text):
    """Searches for an expression in text"""
    if not text:
        text = input()
    match = re.search(expression, text)
    print(match.group())