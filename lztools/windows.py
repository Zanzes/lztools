import sys, os, subprocess

def build_poweroff(reboot:bool):
    cmd = "/mnt/c/Windows/System32/shutdown.exe"
    if reboot:
        cmd = f"{cmd} /r"
    else:
        cmd = f"{cmd} /s"
    return f"{cmd} /t 0"

def poweroff(reboot:bool):
    os.system(build_poweroff(reboot))

def is_active_system(subsystem_valid:bool=True) -> bool:
    if sys.platform == "win32":
        return True
    elif subsystem_valid and sys.platform == "linux":
        return "microsoft" in subprocess.getoutput("uname -r").lower()
    return False

def if_windows(func:exec, subsystem_valid:bool=True):
    if is_active_system(subsystem_valid):
        return func()