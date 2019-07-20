import os
from subprocess import run, getoutput

def command(cmd, *args, return_result=False):
    if return_result:
        return _command_result(cmd, *args)
    else:
        _command(cmd, *args)

def _command_result(cmd, *args):
    try:
        return getoutput(cmd)
    except:
        result = run([cmd, *args], capture_output=True, universal_newlines=True)
        return result.stdout

def _command(cmd, *args, return_result=False):
    fargs = " ".join(args)
    c = f"{cmd} {fargs}"
    print(c)
    os.system(c)