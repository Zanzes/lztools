import os
import subprocess

import sys
from types import FunctionType

from lztools import lzglobal


def build_poweroff(reboot:bool, sudo:bool):
    cmd = "systemctl"
    if sudo:
        cmd = f"sudo {cmd}"
    if reboot:
        cmd = f"{cmd} reboot"
    else:
        cmd = f"{cmd} poweroff"
    return cmd


def poweroff(reboot:bool, sudo:bool):
    os.system(build_poweroff(reboot, sudo))

def require_apt_package(package:str, skip_system_check:bool=False):
    if skip_system_check or is_active_system():
        out = subprocess.getstatusoutput(f'sudo apt list --installed | grep "{package}/"')
        if not out[0] == 0:
            print(f"This program requires the package '{package}'' quiting!")
            print(f"Running 'sudo apt install --install-recommends {package}' may fix this.")
            quit(1)

def is_active_system() -> bool:
    return sys.platform == "linux"

def if_linux(func:exec):
    if is_active_system():
        func()
