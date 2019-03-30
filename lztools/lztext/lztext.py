import ast
import inspect
import random
import re
import string
import time
import uuid
from datetime import datetime
from typing import Union


from . import export
from .match_pairs import MatchPair
from ansiwrap import wrap


_words = None

@export
def words():
    global _words
    from bash import command
    if _words is None:
        _words = command("cat", "/usr/share/dict/words", return_result=True)
    return _words

def _get_alignment(alignment:str) -> str:
    if alignment in ["<", "l", "left"]:
        return "<"
    elif alignment in [">", "r", "right"]:
        return ">"
    elif alignment in ["^", "c", "center"]:
        return "^"
    else:
        raise ValueError("Alignment argument not understood")
def _get_padding(padding:int, char:str=" ") -> str:
    result = ""
    for _ in range(0, padding, len(char)):
        result += char
    return result

@export
def create_line(char:str= "-", width:int=200, text:str= "") -> str:
    o = pad_length(text, width, text_alignment="<", pad_char=char)
    return o

# def center_on(value:str, lztext:str) -> str:
#     return u"{:^{}}".format(value, len(lztext))

@export
def pad(text, count, pad_char, text_alignment):
    alignment = _get_alignment(text_alignment)
    if alignment == "^":
        while lz_ansi.true_length(text) < count:
            text += pad_char
            if lz_ansi.true_length(text) < count:
                text = pad_char + text
    elif alignment == "<":
        while lz_ansi.true_length(text) < count:
            text += pad_char
    elif alignment == ">":
        while lz_ansi.true_length(text) < count:
            text = pad_char + text

@export
def pad_length(text:str, width:int, text_alignment:str, pad_char=" ") -> str:
    alignment = _get_alignment(text_alignment)
    if alignment == "^":
        while lz_ansi.true_length(text) < width:
            text += pad_char
            if lz_ansi.true_length(text) < width:
                text = pad_char + text
    elif alignment == "<":
        while lz_ansi.true_length(text) < width:
            text += pad_char
    elif alignment == ">":
        while lz_ansi.true_length(text) < width:
            text = pad_char + text
    return text

@export
def wall_text(text:str, width:int=80, wall:str= "|", text_alignment="<", h_padding=2, colorizer=None) -> str:
    pad = _get_padding(h_padding)
    text_alignment = _get_alignment(text_alignment)

    result, adjusted = "", width - len(wall) * 2 - h_padding * 2
    executed = False
    for lt in text.splitlines():
        for line in wrap(lt, width=adjusted):
            if colorizer:
                line = colorizer(line)
            executed = True
            line = pad_length(line, adjusted, text_alignment)
            if line == "":
                line = " "
            result += "{}{}{:{}{}}{}{}\n".format(wall, pad, line, text_alignment, adjusted, pad, wall)
    if not executed:
        result = "{}{}{:{}{}}{}{}\n".format(wall, pad, " ", text_alignment, adjusted, pad, wall)
    return result[:-1]

@export
def box_text(text:str, width:int=80, roof:str= "-", wall:str= "|", text_alignment="<") -> str:
    line = pad_length("", width=width, text_alignment=text_alignment, pad_char=roof)
    walled = wall_text(text, wall=wall, text_alignment=text_alignment)
    return f"{line}\n{walled}\n{line}"


@export
def regex(expr:str, text:str, only_first:bool=False, suppress:bool=False) -> str:
    if not only_first:
        return _regex(expr, text, only_first, suppress)
    else:
        try:
            return _regex(expr, text, only_first, suppress).__next__()
        except Exception as e:
            if not suppress:
                raise

def _regex(expr:str, text:str, only_first:bool=False, suppress:bool=False) -> str:
    gen = (x for x in re.findall(expr, text))
    if only_first:
        if suppress:
            try:
                yield gen.__next__()
            except:
                pass
        else:
            yield gen.__next__()
    else:
        yield from gen

@export
def wrap_lines(text: str, width: int = 80) -> str:
    for line in text.splitlines():
        yield from (line[i:i + width] for i in range(0, len(line), width))


@export
def insert_spaces(name:str, underscore:str="") -> str:
    s, n = u"", name[:-4]
    s = s.replace(u"_", underscore)[:-1]
    n = re.sub(r"(?<=\w)([A-Z])", r" \1", str(n))
    return u"{}{}".format(s, n)

# def trim_end(remove:str, the_text:str) -> str:
#     while the_text.endswith(remove):
#         the_text = the_text[:-len(remove)]
#     return the_text

# def format_seconds(sec:Union[int, float, str]) -> str:
#     return time.strftime('%H:%M:%S', time.gmtime(sec))

@export
def search_words(term, strict=False):
    for word in words():
        if strict:
            if term in word:
                yield word
        else:
            pas = True
            for l in set(term):
                if l not in word:
                    pas = False
            if pas:
                yield word

@export
def get_random_word():
    return random.choice(list(words()))

def _is_escaped(text, index) -> bool:
    def __is_escaped(t, i, v) -> bool:
        if t[i-1] == "\\":
            return __is_escaped(t, i-1, not v)
        else:
            return v
    return __is_escaped(text, index, False)


@export
def find_matching(match_type:Union[MatchPair, str], text:str, offset:int=0, raise_error:bool=True, fail_value=-1) -> int:
    if match_type is brace or match_type == "{":
        open, close = brace
    elif match_type is bracket or match_type == "[":
        open, close = bracket
    elif match_type is parentheses or match_type == "(":
        open, close = parentheses
    elif match_type is gt_lt or match_type == "<":
        open, close = gt_lt
    else:
        raise ValueError(f"Argument 'match_type' value '{match_type}' not understood.\n'match_type' must be either {{, [, (, < or one of the values from MatchPair.")

    depth = 0
    skipping:bool = False
    for i, c in enumerate(text):
        if i < offset:
            continue
        if not skipping:
            if c == '"' and not _is_escaped(text, i):
                skipping = True
            if c == open:
                depth += 1
            if c == close:
                if depth > 0:
                    depth -= 1
                else:
                    return i
        elif skipping and c == '"' and not _is_escaped(text, i):
            skipping = False
    if raise_error:
        raise LookupError("Closing brace not found")
    return fail_value

def as_literal(*args, **kwargs) -> str:
    f = inspect.currentframe().f_back
    filename = inspect.getfile(f)
    code_line = open(filename).readlines()[f.f_lineno - 1]
    t = f"{as_literal.__name__}("
    i = code_line.find(t) + len(t)
    e = find_matching(parentheses, code_line, offset=i)
    return code_line[i:e]


@export
def print_collection(obj):
    _print_collection(obj)

def _print_collection(ob, i=0):
    indent = "".join(["\t" for _ in range(i)])
    if type(ob) == list or type(ob) == tuple:
        for i, x in enumerate(ob):
            res = f"{indent}{i}:"
            if is_collection(x):
                print(res)
                _print_collection(x, i)
            else:
                print(f"{res} {x}")
    elif type(ob) == dict:
        for key in ob:
            o = ob[key]
            res = f"{indent}{key}:"
            if type(o) in [list, dict, tuple]:
                print(res)
                _print_collection(o, i + 1)
            else:
                print(f"{res} {o}")
    else:
        print(ob)

@export
def print_dict(obj):
    def pd(ob, i=0):
        indent = "".join(["\t" for _ in range(i)])
        for key in ob.__dict__:
            o = ob.__dict__[key]
            res = f"{indent}{key}:"
            if is_collection(o):
                print(res)
                _print_collection(o, i + 1)
            else:
                print(f"{res} {o}")

    pd(obj)

@export
def is_collection(obj):
    return type(obj) in [list, dict, tuple]

@export
def print_dir_values(obj):
    def pd(ob, i=0):
        indent = "".join(["\t" for _ in range(i)])
        for key in dir(ob):
            o = getattr(ob, key)
            res = f"{indent}{key}:"
            if is_collection(o):
                print(res)
                _print_collection(o, i + 1)
            else:
                print(f"{res} {o}")

    pd(obj)

@export
def parse_name_list(name_list):
    rset = {}
    for setting in name_list:
        key, value = setting.split("=", 1)
        if value.isdigit():
            if value.isdecimal():
                value = float(value)
            else:
                value = int(value)
        elif value.lower() == "true":
            value = bool(value)
        rset[key] = value
    return rset


@export
def line(width=160, separator="-", text=""):
    try:
        o = f"{text:{separator}<{width}}"
    except UnicodeEncodeError as ex:
        if ex.message:
            ex.message += text
        elif ex.msg:
            ex.msg += text
        raise ex
    return o

@export
def format_seconds(sec):
    return time.strftime('%H:%M:%S', time.gmtime(sec))

@export
def center_on(value, text):
    return f"{value:^{len(text)}}"

@export
def trim_end(remove, the_text):
    while the_text.endswith(remove):
        the_text = the_text[:-len(remove)]
    return the_text

@export
def format_api_error(message):
    res = message
    if message is not None and message['error_code'] == "invalid_input_data":
        res = "Invalid input data:"
        if len(message['field_errors']) > 0:
            res += "\n"
            for error_key, error in zip(message['field_errors'].keys(), message['field_errors'].values()):
                res += f"\t{error_key}\n"
                res += f"\t\t{error['error_human']}\n"
                if len(error['args']) > 0:
                    for k, v in error.iteritems():
                        res += f"\t\t{k}: {v}\n"
    elif message['error_code'] == "missing_permissions":
        res = f"API Error: {message['error_human']}"
    return res

@export
def format_mission_errors(errors):
    ret = errors
    if isinstance(errors, list):
        ret = ""
        for error in errors:
            ret += f"Code: {error[u'code']}\nError: {error[u'description']}\nModule: {error[u'module']}\n\n"
    return ret

@export
def format_arg_string(string_data):
    ret = string_data
    if "%" in string_data:
        etext = ast.literal_eval(string_data)
        ret = etext['message'] % etext['args']
    return ret

@export
def format_test_name(name):
    s, n = u"", name
    if name.startswith(u"MIRS_"):
        s = re.search("MIRS_\d+_", n).group(0)
        n = u" " + n.replace(s, u"").replace(u"_", u"")
    s = s.replace(u"_", u"-")[:-1]
    n = re.sub(r"(?<=\w)([A-Z0-9])", r" \1", str(n))
    return f"{s}{n}"

@export
def generate_uniqe_date_based_name(date:datetime=None):
    if not date:
        date = datetime.now()
    return f"{date.year}-{date.strftime('%B')}-{date.strftime('%A')}-{date.hour}-{date.minute}-{date.second}-{uuid.uuid4()}"

@export
def generate_uniqe_date_based_name_numeric(date:datetime=None):
    if not date:
        date = datetime.now()
    return f"{date.year}-{date.month}-{date.day}-{date.hour}-{date.minute}-{date.second}-{uuid.uuid4()}"

@export
def generate_text(length=100, safe=False):
    sel = string.ascii_letters + string.digits  # + "æøåÆØÅ" + "𢞵𠝹𡁻𤓓𡃁𠺝𠱓𠺢𠼮𤶸𢳂𢵌𨋢𠹷𩶘𠸏𠲖𦧺𨳒𢯊𡁜𢴈𠵿𠳏𢵧𦉘𠜎𠾴𧨾𢫕𠱸𨳍𡇙𢱕𠻺𠳕𠿪𠻗𠜱𦧲"
    # TODO: Remove '<' and '>' when naming is fixed
    ext = sel + string.punctuation.replace("\\", "").replace("<", "").replace(">", "")

    name = random.choice(sel)
    while len(name) < length:
        if safe:
            name += random.choice(sel)
        else:
            name += random.choice(ext)
    return name