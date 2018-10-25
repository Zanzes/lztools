#!/usr/bin/env python3

import random as rand
from multiprocessing import Queue
from subprocess import call

import click
from click import Context

import lztools.Images
from lztools import Images
from lztools.bash import search_history
from lztools.beautification import rainbow
from lztools.lztools import command
from lztools.text import search_words, get_random_word, regex as rx

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

colorizations = ['none', 'rainbow', 'altbow', 'metal']

q = Queue()

def try_read_input(input):
    try:
        return "\n".join(input.readlines())[:-1]
    except:
        return input

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """A collection of python tools and bash commands by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""

@main.command(context_settings=CONTEXT_SETTINGS)
def morning():
    """Installs updates and so on..."""
    call(["sudo", "apt", "update", "-y"])
    call(["sudo", "apt", "upgrade", "-y"])

# ,.-~*´¨¯¨`*·~-.¸-( ALIAS: MORNING )-,.-~*´¨¯¨`*·~-.¸
@main.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
def m(ctx:Context, *args, **kwargs):
    ctx.forward(morning)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("term")
@click.option("-r", "--regex", is_flag=True, default=False)
def history(term, regex):
    """Search bash history"""
    for line in search_history(term, regex=regex):
        print(line)

# ,.-~*´¨¯¨`*·~-.¸-( ALIAS: HISTORY )-,.-~*´¨¯¨`*·~-.¸
@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("term")
@click.option("-r", "--regex", is_flag=True, default=False)
@click.pass_context
def h(ctx:Context, *args, **kwargs):
    ctx.forward(history)

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
        res = lztools.Images.search(term, count=max_images)
        for x in res:
            print(x)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option('-t', '--type', type=click.Choice(['words', 'images', 'colorization']), default='images', help="Random category")
@click.option("-c", "--count", default=1, help="The number of results")
@click.option("-nn", "--not-nocolor", is_flag=True, default=False, help="Random colorization never selects no color")
@click.argument("input", default=click.get_text_stream('stdin'))
def random(type, count, not_nocolor, input):
    if type == "images":
        res = Images.get_random_image(count=count)
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
@click.argument("start")
@click.argument("end")
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
        for x in rx(expr, input, only_first=single_result, suppress=True):
            print(x)
    else:
        print(rx(expr, input, only_first=single_result, suppress=True))

@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("input")
@click.option('-t', '--type', type=click.Choice(colorizations))
@click.option("-nn", "--not-nocolor", is_flag=True, default=False)
def colorize(input, type, not_nocolor):
    color(input, type, not_nocolor)

@main.command(name="rainbow", context_settings=CONTEXT_SETTINGS)
@click.option("-s", "--speed", type=float, default=20)
@click.option("-f", "--frequency", type=float, default=0.1)
@click.option("-a", "--animate", is_flag=True, default=False)
@click.argument("input", default=click.get_text_stream('stdin'))
def rainbow_cli(speed, frequency, animate, input):
    rainbow(input, speed, frequency, animate)

def color(input, type, not_nocolor):
    if type == 'none':
        print(input)
    elif type == 'rainbow':
        command("toilet", "-f", "term", "--gay", input)
    elif type == 'altbow':
        command("echo \"{}\" | lolcat".format(input))
    elif type == 'metal':
        command("toilet", "-f", "term", "--metal", input)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option("-w", "--width", type=int, default=100)
@click.option("-i", "--invert", is_flag=True, default=False)
@click.option("-c", "--add-color", is_flag=True, default=False)
@click.argument("target")
def art(width, invert, add_color, target):
    args = []

    if invert:
        args.append("-i")
    if add_color:
        args.append("-c")

    args.append("--width")
    args.append(str(width))

    args.append(target)
    if not add_color:
        args.append("| tail -n +2")
    command(f"asciiart", *args)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option('-o', '--operation', type=click.Choice(["bashrc", "autosource"]))
def bash(operation):

    pass

def to_art(url, width, color):
    args = ["art", url, f"-w {str(width-2)}"]
    if color:
        args.append("-c")
        # print("Args: " + " ".join(args))
        return command("lztools", *args, return_result=True)
    else:
        return command("lztools", *args, return_result=True)

@main.command(context_settings=CONTEXT_SETTINGS)
@click.option("-n/-r", "--noire/--rainbow", is_flag=True, default=False)
@click.option("-s", "--speed", type=float, default=None)
@click.option("-f", "--frequency", type=float, default=None)
@click.option("-w", "--width", type=int, default=None)
@click.option("--separate", is_flag=True, default=True)
def fun(noire, speed, frequency, width, separate):
    term_width = width if width else int(command("tput", "cols", return_result=True))

    if not noire:
        for x in Images.get_random_image(count=1):
            n = to_art(x, term_width, True)
            print(rainbow(n, frequency, hide_gap=separate))
    else:
        while True:
            try:
                gi(q, term_width, True)
            except:
                exit()

if __name__ == '__main__':
    main()




