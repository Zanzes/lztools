import datetime
import os
import shutil
from time import sleep
from lztools.dating import hours_minutes_seconds
from lztools.linux.bash import command
from lztools.sound import beep_on_off

_clear = lambda: os.system('_clear')

def _to_timespan(time_str:str):
    tt, tf = time_str[:-1], time_str[-1]
    format = tt.isdigit() and tf.isalpha()
    if time_str.isdigit() or tf == "m" and format:
        return datetime.timedelta(minutes=int(time_str))
    elif ":" in time_str:
        h, m = time_str.split(":")
        h, m = int(h), int(m)
        n = datetime.datetime.now()
        t = n.replace(hour=h, minute=m)
        if t < n:
            t = t.replace(day=t.day+1)
        return t - datetime.datetime.now()
    elif tf == "s" and format:
        return datetime.timedelta(seconds=int(tt))
    elif tf == "h" and format:
        return datetime.timedelta(hours=int(tt))
    elif tf == "d" and format:
        return datetime.timedelta(days=int(tt))
    else:
        raise Exception("Unable to parse time argument")

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