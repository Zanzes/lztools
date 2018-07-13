from builtins import map

import click
import collections

import lztools.Data.Images

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """A collection of python tools and bash commands by laz aka nea"""

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option("-c", "--count", default=1)
@click.option("-s", "--search", default=None)
@click.option("-v/-q", "--verbose/--quiet", default=False)
def picture(count, search, verbose):
    if search is not None:
        res = lztools.Data.Images.search(search, count, verbose=verbose)
        for x in res:
            print(x)
    else:
        for _ in range(count):
            print(lztools.Data.Images.get_random_image(verbose=verbose))

@main.command(context_settings=CONTEXT_SETTINGS)
def text():
    """Get or generate text"""





# @main.command(context_settings=CONTEXT_SETTINGS)
# @click.option('--data-type', type=click.Choice(['picture', 'text']), default='picture', help="The data type to work with")
# def data(data_type):
#     """Get or generate data"""
#     if data_type == 'picture':
#         print("pic {}".format(data_type))
#     elif data_type == 'text':
#         print("text {}".format(data_type))
#     else:
#         print("Invalid argument (--data-type = {})".format(data_type))