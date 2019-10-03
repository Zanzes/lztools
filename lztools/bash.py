import os
from subprocess import run, getoutput

from lztools.enums import ClipboardBuffer

def command(cmd, *args, return_result=False):
    if return_result:
        return _command_result(cmd, *args)
    else:
        _command(cmd, *args)

def _command_result(cmd, *args):
    try:
        c = cmd + " " + " ".join(args)
        return getoutput(c)
    except:
        result = run([cmd, *args], capture_output=True, universal_newlines=True)
        return result.stdout

def _command(cmd, *args, return_result=False):
    fargs = " ".join(args)
    c = f"{cmd} {fargs}"
    print(c)
    os.system(c)

def get_clipboard_content(buffer:ClipboardBuffer=ClipboardBuffer.primary):
    return command("xclip", "-sel", buffer, "-o", return_result=True)