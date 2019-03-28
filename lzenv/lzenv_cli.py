import click

from lzenv import run

@click.command()
def start():
    run()