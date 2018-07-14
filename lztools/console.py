#!/usr/bin/env python3
import random as rand
import click
import lztools.Data.Images
from lztools.Data.Text import get_random_word, search_words

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """A collection of python tools and bash commands by laz aka nea"""

if __name__ == '__main__':
    main()

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option("-c", "--count", default=1)
@click.option("-v/-q", "--verbose/--quiet", default=False)
@click.argument("search", default="")
def picture(count, search, verbose):
    if search is not None and search != "":
        res = lztools.Data.Images.search(search, count, verbose=verbose)
        for x in res:
            print(x)
    else:
        res = lztools.Data.Images.get_random_image(verbose=verbose, count=count)
        for x in res:
            print(x)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option("-r", "--random", is_flag=True, default=False)
@click.option("-s", "--strict", is_flag=True, default=False)
@click.argument("search", default="")
def text(random, strict, search):
    """Get or generate text"""
    if random and search == "":
        print(get_random_word())
    else:
        res = search_words(search, strict=strict)
        if random:
            print(rand.choice(list(res)))
        else:
            for w in res:
                print(w)

@main.group(context_settings=CONTEXT_SETTINGS)
def ascii():
    """fun"""







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