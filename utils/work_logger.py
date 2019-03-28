import datetime
from pathlib import Path

import lzresources
from pytools.mod_tools import get_module_path

resources_path = Path(get_module_path(lzresources))

def log_work():
    dt = datetime.datetime.now()
    fp:Path = resources_path.joinpath(f"{dt.year}-{dt.month}-{dt.day}.data")
    if not fp.exists():
        fp.touch()
    if get_wifi_network_name() == "mir-main":
        with fp.open("a") as f:
            f.write(dt)
            print(f"Logged as working at {dt}")
    else:
        print("You do not seem to be at work")

def print_work():
    ever_worked = False
    for file in resources_path.glob("*.data"):
        ever_worked = True
        print(file)
    if not ever_worked:
        print(f"You never have bin recorded as being at work... Slagger! :p")

if __name__ == '__main__':
    log_work()