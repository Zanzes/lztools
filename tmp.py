from time import sleep

import system_hotkey

hk = system_hotkey.SystemHotkey()

hk.register(('control', 'shift', 'z'), callback=lambda: print("xxxx"))
while 1:
    sleep(1)