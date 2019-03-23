import click

from core.click import command_matching_group
from core.ResourceManager import out_path

@command_matching_group()
def main():
    pass

@click.command()
def has_output():
    print(out_path.stat().st_size > 0)