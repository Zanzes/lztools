import datetime
import os
import shutil
from time import sleep
from lztools.timing_and_dating import hours_minutes_seconds
from lztools.bash import command
from lztools.sound import beep_on_off

_clear = lambda: os.system('_clear')

def start_alarm(time:datetime.timedelta, in_window=False):
    end = datetime.datetime.now() + time
    while end > datetime.datetime.now():
        l = end - datetime.datetime.now()
        h, m, s = hours_minutes_seconds(l)
        _clear()
        e = ""
        if l.days > 0:
            e = f"{e}{l.days} Days and "
        if h > 0:
            e = f"{e}{h:02}:"
        if m > 0:
            e = f"{e}{m:02}:"
        command("figlet", f"{e}{s:02}", "-w", shutil.get_terminal_size().columns, "-c")
        # print(figlet(f"{e}{s:02}", w=shutil.get_terminal_size().columns, c=True))
        sleep(0.1)
    beep_on_off(9999, 0.5, 880)