from lztools import linux, windows

def execute(on_linux:exec, on_windows:exec):
    if linux.is_active_system():
        return on_linux()
    elif windows.is_active_system():
        return on_windows()