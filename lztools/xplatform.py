from platform import system,uname

from lztools import linux, windows
from lztools.enums import OS

def execute(on_linux:exec, on_windows:exec, subsystem_valid:bool=False):
    if linux.is_active_system(subsystem_valid):
        return on_linux()
    elif windows.is_active_system(not subsystem_valid):
        return on_windows()

def poweroff(reboot, sudo):
    execute(linux.poweroff(reboot, sudo), windows.poweroff(reboot))

def identify():
    syst = system().lower()
    if 'cygwin' in syst:
        return OS.Cygwin
    elif 'darwin' in syst:
        return OS.Mac
    elif 'linux' in syst:
        if 'Microsoft' not in uname().release:
            return OS.Linux
        return OS.WSL
    elif 'windows' in syst:
        return OS.Windows
    elif 'bsd' in syst:
        return OS.Bsd


