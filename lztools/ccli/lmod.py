#!/usr/bin/env python3

import zlick

from linux.bash import add_bashrc_alias, copy_bashrc_other
from zlick import proper_group, proper_command

@proper_group()
def main():
    """A collection of python tools and bash commands for manipulating text by laz aka nea"""

@proper_command()
@zlick.argument("line")
@zlick.option('-t', '--type', type=zlick.Choice(["alias", "export", "variable", "other"]), default="other")
def rcadd(line, type):
    """Adds a line to .bashrc"""
    if type == "alias":
        add_bashrc_alias(line)


@proper_command()
@zlick.option("-t/-f", "--to-me/--from-me", is_flag=True, default=False)
@zlick.option("-o", "--out", nargs=1, type=str, default=None)
def rccopy(to_me, out):
    """Adds a line to .bashrc"""
    copy_bashrc_other(to_me, out_path=out)


