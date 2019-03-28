#!/usr/bin/env python3
import click
import zlick
from zlick import command_matching_group

@command_matching_group()
def main():
    """A collection of python tools and bash commands for manipulating text by laz aka nea"""

@zlick.command()
@click.argument("line")
@click.option('-t', '--type', type=zlick.Choice(["alias", "export", "variable", "other"]), default="other")
def rcadd(line, type):
    """Adds a line to .bashrc"""
    if type == "alias":
        add_bashrc_alias(line)


@zlick.command()
@click.option("-t/-f", "--to-me/--from-me", is_flag=True, default=False)
@click.option("-o", "--out", nargs=1, type=str, default=None)
def rccopy(to_me, out):
    """Adds a line to .bashrc"""
    copy_bashrc_other(to_me, out_path=out)


