import sys

from text_tools import lz_ansi

def add_stdin_arg(name, parser):
    parser.add_argument(name, nargs="*", default=sys.stdin, type=str)

def parse_stdin_arg(value):
    prep = (lambda x: x[:-1]) if type(value).__name__ == "file" else (lambda x: x)
    return (lz_ansi.strip_reg(prep(x)) for x in value)