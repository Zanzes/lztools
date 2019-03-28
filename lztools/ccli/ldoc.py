#!/usr/bin/env python3
from zlick import command_matching_group

import zlick, click

from third.docker import get_running

@command_matching_group()
def main():
    """A collection of python tools and bash commands for git by Laz aka nea"""
    pass

@zlick.command()
@click.option("-a" "--all", is_flag=True, default=True)
@click.option("-l" "--list", is_flag=True, default=True)
def kill():
    """test"""
    get_running()
    pass

@zlick.command()
@click.option("-a" "--all", is_flag=True, default=True)
def run():
    """test"""
    pass

