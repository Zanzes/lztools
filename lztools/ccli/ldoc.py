#!/usr/bin/env python3

import zlick

from third.docker import get_running
from zlick import proper_group, proper_command

@proper_group()
def main():
    """A collection of python tools and bash commands for git by Laz aka nea"""
    pass

@proper_command()
@zlick.option("-a" "--all", is_flag=True, default=True)
@zlick.option("-l" "--list", is_flag=True, default=True)
def kill():
    """test"""
    get_running()
    pass

@proper_command()
@zlick.option("-a" "--all", is_flag=True, default=True)
def run():
    """test"""
    pass

