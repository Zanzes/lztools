import sys, os

from lztools import lzglobal

def build_poweroff(reboot:bool):
    cmd = "/mnt/c/Windows/System32/shutdown.exe"
    if reboot:
        cmd = f"{cmd} /r"
    else:
        cmd = f"{cmd} /s"
    return f"{cmd} /t 0"


def poweroff(reboot:bool):
    os.system(build_poweroff(reboot))

def is_active_system() -> bool:
    return sys.platform == "win32"

def if_windows(func:exec):
    if is_active_system():
        func()