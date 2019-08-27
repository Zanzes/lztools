from lztools import zlick
from lztools import pytools

@zlick.command_matching_group()
def main():
    """Tools to make python development more convenient"""

@main.command()
def cleanup_temporary():
    """Removes temporary files leftover after build"""
    pytools.cleanup_build_files()

@main.command()
def install_module():
    """Installs a python module  """
    pytools.cleanup_build_files()