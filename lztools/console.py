#!/usr/bin/env python3
import random as rand

import click
import os

import lztools.Data.Images
from Resources.Requirements import apt_requires
from lztools.Bash import return_command_result, execute_command
from lztools.Data import Text
from lztools.Data.Text import get_random_word, search_words

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

colorizations = ['none', 'rainbow', 'altbow', 'metal']

def try_read_input(input):
    try:
        return "\n".join(input.readlines())[:-1]
    except:
        return input

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """A collection of python tools and bash commands by laz aka nea"""

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("term", default="")
@click.option('-t', '--type', type=click.Choice(['words', 'images']), help="The type of search")
@click.option("-s", "--strict", is_flag=True, default=False, help="Indicates that letters has to appear in the same order as the do in TERM")
@click.option("-m", "--max-images", default=1, type=click.IntRange(1, 500), help="Max number of images")
def search(term, type, strict, max_images):
    if type == "words":
        res = search_words(term, strict=strict)
        print(res)
    elif type == "images":
        res = lztools.Data.Images.search(term, count=max_images)
        for x in res:
            print(x)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option('-t', '--type', type=click.Choice(['words', 'images', 'colorization']), default='images', help="Random category")
@click.option("-c", "--count", default=1, help="The number of results")
@click.option("-nn", "--not-nocolor", is_flag=True, default=False, help="Random colorization never selects no color")
@click.argument("input", default=click.get_text_stream('stdin'), help="The input")
def random(type, count, not_nocolor, input):
    if type == "images":
        res = lztools.Data.Images.get_random_image(count=count)
        for x in res:
            print(x)
    elif type == "words":
        for _ in range(count):
            print(get_random_word())
    elif type == "colorization":
        choices = colorizations
        input = try_read_input(input)
        if not_nocolor:
            choices = colorizations[1:]
        color(input, rand.choice(choices), not_nocolor=not_nocolor)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("input", nargs=-1)
@click.option("-d", "--delimiter", nargs=1, help="The delimiter to split the input by")
def split(input, delimiter):
    i = str.join("\n", input).strip()
    if delimiter:
        i = i.split(delimiter)
    else:
        i = i.splitlines()
    for x in i:
        print(x)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("start", help="The first indicator")
@click.argument("end", help="The second indicator")
@click.argument("Text", default=click.get_text_stream('stdin'))
@click.option("-p", "--partial-matches", is_flag=True, default=False, help="Used if indicators are not complete lines")
def cut(start, end, text, partial_matches):
    p = False
    for l in text.splitlines():
        if partial_matches:
            if end in l:
                p = False
        else:
            if l == end:
                p = False
        if p:
            print(l)
        if partial_matches:
            if start in l:
                p = True
        else:
            if l == start:
                p = True

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("expr")
@click.argument("Text", default=click.get_text_stream('stdin'))
@click.option("-s", "--single-result", is_flag=True, default=False)
def regex(expr, text, single_result):
    input = try_read_input(text)
    print(input, expr)
    if not single_result:
        for x in Text.regex(expr, input, only_first=single_result, suppress=True):
            print(x)
    else:
        print(Text.regex(expr, input, only_first=single_result, suppress=True))

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("input")
@click.option('-t', '--type', type=click.Choice(colorizations))
@click.option("-nn", "--not-nocolor", is_flag=True, default=False)
def colorize(input, type, not_nocolor):
    color(input, type, not_nocolor)

def color(input, type, not_nocolor):
    if type == 'none':
        print(input)
    elif type == 'rainbow':
        print(return_command_result("toilet", "-f", "term", "--gay", input))
    elif type == 'altbow':
        execute_command("echo \"{}\" | lolcat".format(input))
    elif type == 'metal':
        print(return_command_result("toilet", "-f", "term", "--metal", input))

@main.command(context_settings=CONTEXT_SETTINGS)
def install():
    execute_command("sudo apt install -y {}".format(str.join(" ", apt_requires)))

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option('-o', '--operation', type=click.Choice(["bashrc", "autosource"]))
def bash(operation):

    pass

if __name__ == '__main__':
    main()




# @main.command(context_settings=CONTEXT_SETTINGS)
# @click.option("-r", "--random", "operation", default=False, flag_value="random")
# @click.option("-s", "--strict", "operation", default=False, flag_value="strict")
# @click.option("-d", "--division", "operation", default=False, flag_value="division")
# @click.option("-fr", "--find-regex", "operation", default=False, flag_value="regex")
# @click.option("-f", "--find", "operation", default=True, flag_value="search")
# @click.argument("search", nargs=-1)
# def text(operation, search):
#     print(operation, search)
#     exit()
#     """Get or generate text"""
#     if operation == "random":
#         pass
#     elif operation == "strict":
#         pass
#     elif operation == "division":
#         pass
#     elif operation == "regex":
#         pass
#     elif operation == "search":
#         ss = search.split(search)
#         for part in ss:
#             if part is not None and part != "":
#                 print(part)
#     elif operation == "random" and search == "":
#     else:
#         res = search_words(search, strict=strict)
#         if random:
#             print(rand.choice(list(res)))
#         else:
#             for w in res:
#                 print(w)

# @main.command(context_settings=CONTEXT_SETTINGS)
# @click.argument("PATH")
# @click.option("-c/-m", "--color/--monochrome", default=False)
# @click.option("-w", "--width", default=100, type=click.IntRange(1, 500))
# @click.option("-i", "--invert", is_flag=True, default=False)
# def art(path, color, width, invert):
#     """fun"""
#     args = ["--width", str(width), path]
#     if color:
#         args.append("-c")
#     if invert:
#         args.append("-i")
#     command = ["asciiart", *args]
#     print("Command: {}".format(command))
#     print(subprocess.check_call(command))




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