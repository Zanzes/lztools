import os
import subprocess
import sys

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
    if skip_system_check or is_active_system(True):
        out = subprocess.getstatusoutput(f'sudo apt list --installed | grep "{package}/"')
        if not out[0] == 0:
            print(f"This program requires the package '{package}'' quiting!")
            print(f"Running 'sudo apt install --install-recommends {package}' may fix this.")
            quit(1)

def is_active_system(subsystem_valid:bool=False) -> bool:
    if not subsystem_valid:
        return sys.platform == "linux" and "microsoft" not in subprocess.getoutput("uname -r").lower()
    return sys.platform == "linux"

def if_linux(func:exec, subsystem_valid:bool=False):
    if is_active_system(subsystem_valid):
        return func()
