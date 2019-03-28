import zlick

from zlick import command_matching_group
from core.ResourceManager import out_path

@command_matching_group()
def main():
    pass

@zlick.command()
def has_output():
    print(out_path.stat().st_size > 0)