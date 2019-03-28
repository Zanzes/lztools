#!/usr/bin/env python3
import itertools
import os
import random as rand
import subprocess
from multiprocessing import Queue
from subprocess import call

import zlick

from core import Images
import lzconstants
from third import docker
from linux import bashrc
from text_tools import lztext
from linux.bash import command
from linux.bashrc import search_history
from core.beautification import rainbow
from zlick import CommandMatchingGroup, command_matching_group
from text_tools.lztext import search_words, get_random_word, regex as rx

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

colorizations = ['none', 'rainbow', 'altbow', 'metal']

q = Queue()

def try_read_input(input):
    try:
        return "\n".join(input.readlines())[:-1]
    except:
        return input


@command_matching_group()
def main():
    """A collection of python tools and bash commands by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""

@main.command(context_settings=CONTEXT_SETTINGS)
def morning():
    """Installs updates and so on..."""
    call(["sudo", "apt", "update", "-y"])
    call(["sudo", "apt", "upgrade", "-y"])

@main.command(context_settings=CONTEXT_SETTINGS)
@zlick.argument("term")
@zlick.option("-r", "--regex", is_flag=True, default=False)
def history(term, regex):
    """Search bash history"""
    for line in search_history(term, regex=regex):
        print(line)

@main.group(context_settings=CONTEXT_SETTINGS, cls=CommandMatchingGroup)
def files():
    pass

@files.command(context_settings=CONTEXT_SETTINGS)
@zlick.argument('FIND')
@zlick.argument('REPLACEMENT')
@zlick.option("-p", "--path", default=".", type=str, help="The path f or search for files (Default: .)")
def replace(find, replacement, path):
    """Searches files in --path for the term in FIND and replaces occurrences with REPLACEMENT"""
    os.system(f"find {path} -type f -exec sed -i 's/{find}/{replacement}/g' {{}} +")

@files.command(context_settings=CONTEXT_SETTINGS)
@zlick.argument('FIND')
@zlick.option("-p", "--path", default=".", type=str, help="The path for search for files (Default: .)")
@zlick.option("-e", "--exclude", default="*.git", type=Path(), help="Path not included in search (Default: *.git)")
def search(find, path, exclude):
    """Searches for FIND in --path"""
    os.system(f"grep -Rnw '{path}' --color=auto --exclude \"*.pyc\" --exclude-dir \"{exclude}\" -e '{find}'")

@files.command(context_settings=CONTEXT_SETTINGS)
@zlick.argument('PATTERN')
@zlick.option("-p", "--path", default=".", type=str, help="The path for search for files (Default: .)")
# @click.option("-e", "--exclude", default="*.git", type=Path(), help="Path not included in search (Default: *.git)")
def find(pattern, path):
    # os.system(f"find {path} -type f -exec sed -i 's/{find}/{replacement}/g' {{}} +")
    pass

@main.command(context_settings=CONTEXT_SETTINGS)
@zlick.argument("term", default="")
@zlick.option('-t', '--type', type=zlick.Choice(['words', 'images']), help="The type of search")
@zlick.option("-s", "--strict", is_flag=True, default=False, help="Indicates that letters has to appear in the same order as the do in TERM")
@zlick.option("-m", "--max-images", default=1, type=zlick.IntRange(1, 500), help="Max number of images")
def search(term, type, strict, max_images):
    if type == "words":
        res = search_words(term, strict=strict)
        print(res)
    elif type == "images":
        res = Images.search(term, count=max_images)
        for x in res:
            print(x)

@main.command(context_settings=CONTEXT_SETTINGS)
@zlick.option('-t', '--type', type=zlick.Choice(['words', 'images', 'colorization']), default='images', help="Random category")
@zlick.option("-c", "--count", default=1, help="The number of results")
@zlick.option("-nn", "--not-nocolor", is_flag=True, default=False, help="Random colorization never selects no color")
@zlick.argument("input", default=zlick.get_text_stream('stdin'))
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
@zlick.argument("input", nargs=-1)
@zlick.option("-d", "--delimiter", nargs=1, help="The delimiter to split the input by")
def split(input, delimiter):
    i = str.join("\n", input).strip()
    if delimiter:
        i = i.split(delimiter)
    else:
        i = i.splitlines()
    for x in i:
        print(x)

@main.command(context_settings=CONTEXT_SETTINGS)
@zlick.argument("start")
@zlick.argument("end")
@zlick.argument("Text", default=zlick.get_text_stream('stdin'))
@zlick.option("-p", "--partial-matches", is_flag=True, default=False, help="Used if indicators are not complete lines")
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
@zlick.argument("expr")
@zlick.argument("Text", default=zlick.get_text_stream('stdin'))
@zlick.option("-s", "--single-result", is_flag=True, default=False)
def regex(expr, text, single_result):
    input = try_read_input(text)
    print(input, expr)
    if not single_result:
        for x in rx(expr, input, only_first=single_result, suppress=True):
            print(x)
    else:
        print(rx(expr, input, only_first=single_result, suppress=True))

@main.command(context_settings=CONTEXT_SETTINGS)
@zlick.argument("input")
@zlick.option('-t', '--type', type=zlick.Choice(colorizations))
@zlick.option("-nn", "--not-nocolor", is_flag=True, default=False)
def colorize(input, type, not_nocolor):
    color(input, type, not_nocolor)

@main.command(name="rainbow", context_settings=CONTEXT_SETTINGS)
@zlick.option("-s", "--speed", type=float, default=20)
@zlick.option("-f", "--frequency", type=float, default=0.1)
@zlick.option("-a", "--animate", is_flag=True, default=False)
@zlick.argument("input", default=zlick.get_text_stream('stdin'))
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
@zlick.option("-w", "--width", type=int, default=100)
@zlick.option("-i", "--invert", is_flag=True, default=False)
@zlick.option("-c", "--add-color", is_flag=True, default=False)
@zlick.argument("target")
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
@zlick.option('-o', '--operation', type=zlick.Choice(["bashrc", "autosource"]))
def bash(operation):
    pass

@main.group(cls=CommandMatchingGroup, context_settings=CONTEXT_SETTINGS)
def docker():
    """Operations for interacting with docker"""

@docker.command(context_settings=CONTEXT_SETTINGS)
def cleanup():
    docker.cleanup()

@docker.command(context_settings=CONTEXT_SETTINGS)
@zlick.argument("NAME")
def run(name):
    command(f"sudo docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -u zanzes --tty --rm {name}")

@main.group(cls=CommandMatchingGroup, context_settings=CONTEXT_SETTINGS)
def rc():
    """Operations for interacting with .bashrc"""

# @rc.command(context_settings=CONTEXT_SETTINGS)
# @click.argument("VALUE")
# def add(value):
#     print(value)

@rc.command(context_settings=CONTEXT_SETTINGS)
@zlick.argument("NAME", default=lzconstants.SENTINEL_MARKER)
@zlick.option("-a", "--all", default=False, is_flag=True)
@zlick.option("-l", "--list-sections", default=False, is_flag=True)
@zlick.option("-i", "--include-padding", default=False, is_flag=True)
def show(name, all, list_sections, include_padding):
    if all:
        rcdata = bashrc.read_bash_rc()
        print(rcdata)
    elif list_sections or name == lzconstants.SENTINEL_MARKER:
        if list_sections or name == lzconstants.SENTINEL_MARKER:
            print("Sections:")
            for i, line in enumerate(bashrc.get_section_names(), 1):
                print(f"{lztext.pad_length()}{i}. {line}")
    elif name != lzconstants.SENTINEL_MARKER:
        print(bashrc.get_section(name, include_padding))

# @rc.command(context_settings=CONTEXT_SETTINGS)
# @click.argument("VALUE")
# def replace(value):
#     home = subprocess.getoutput("echo $HOME")
#     rcdata = subprocess.getoutput("cat $HOME/.bashrc")
#     data = rcdata.splitlines()
#     taken = itertools.takewhile(lambda line: line != "# ▂▃▅▇█▓▒░LAZ░▒▓█▇▅▃▂", data)
#     lines = []
#     lines.extend(taken)
#     lines.append("# ▂▃▅▇█▓▒░LAZ░▒▓█▇▅▃▂")
#     lines.append("")
#     lines.append(value)
#     text = "\n".join(lines)
#     print(text)
#     if click.confirm(f"Overwrite old bashrc? ({home}/.bashrc)"):
#         with open(home + "/.bashrc", "w") as f:
#             f.write(text)

@rc.command(context_settings=CONTEXT_SETTINGS, name="get-section")
@zlick.argument("NAME", default=lzconstants.SENTINEL_MARKER)
@zlick.option("-l", "--list", default=False, is_flag=True)
@zlick.option("-f", "--full-section", default=False, is_flag=True)
def get_section(name, list, full_section):
    rcdata = subprocess.getoutput("cat $HOME/.bashrc")
    if list or name == lzconstants.SENTINEL_MARKER:
        for line in rcdata.splitlines():
            if line.endswith(" " + lzconstants.RC_SECTION_START_RIGHT):
                line = line.replace(" " + lzconstants.RC_SECTION_START_RIGHT, "")
                line = line.replace(lzconstants.RC_SECTION_START_LEFT + " ", "")
                print(line)
    elif name != lzconstants.SENTINEL_MARKER:
        taken = rcdata.split(f"{lzconstants.RC_SECTION_START_LEFT} {name} {lzconstants.RC_SECTION_START_RIGHT}", 1)[1]
        taken = taken.split(f"{lzconstants.RC_SECTION_END_LEFT} {name} {lzconstants.RC_SECTION_END_RIGHT}", 1)[0]
        if full_section:
            taken = f"""# {lzconstants.RC_SECTION_START_LEFT} {name} {lzconstants.RC_SECTION_START_RIGHT}
{taken}
{lzconstants.RC_SECTION_END_LEFT} {name} {lzconstants.RC_SECTION_END_RIGHT}"""
        print(taken.strip())

@rc.command(context_settings=CONTEXT_SETTINGS, name="set-section")
@zlick.argument("VALUE")
def set_section(value):
    home = subprocess.getoutput("echo $HOME")
    rcdata = subprocess.getoutput("cat $HOME/.bashrc")
    data = rcdata.splitlines()
    taken = itertools.takewhile(lambda line: line != "# ▂▃▅▇█▓▒░LAZ░▒▓█▇▅▃▂", data)
    lines = []
    lines.extend(taken)
    lines.append("# ▂▃▅▇█▓▒░LAZ░▒▓█▇▅▃▂")
    lines.append("")
    lines.append(value)
    text = "\n".join(lines)
    print(text)
    if zlick.confirm(f"Overwrite old bashrc? ({home}/.bashrc)"):
        with open(home + "/.bashrc", "w") as f:
            f.write(text)

def to_art(url, width, color):
    args = ["art", url, f"-w {str(width-2)}"]
    if color:
        args.append("-c")
        # print("Args: " + " ".join(args))
        return command("lztools", *args, return_result=True)
    else:
        return command("lztools", *args, return_result=True)

@main.command(context_settings=CONTEXT_SETTINGS)
@zlick.option("-n/-r", "--noire/--rainbow", is_flag=True, default=False)
@zlick.option("-s", "--speed", type=float, default=None)
@zlick.option("-f", "--frequency", type=float, default=None)
@zlick.option("-w", "--width", type=int, default=None)
@zlick.option("--separate", is_flag=True, default=True)
def fun(noire, speed, frequency, width, separate):
    term_width = width if width else int(command("tput", "cols", return_result=True))

    if not noire:
        for x in Images.get_random_image(count=1):
            n = to_art(x, term_width, True)
            print(rainbow(n, frequency, hide_gap=separate))
    else:
        while True:
            try:
                pass
                # gi(q, term_width, True)
            except:
                exit()

if __name__ == '__main__':
    main()
