from lztools import linux, windows

def execute(on_linux:exec, on_windows:exec, subsystem_valid:bool=False):
    if linux.is_active_system(subsystem_valid):
        return on_linux()
    elif windows.is_active_system(not subsystem_valid):
        return on_windows()