from subprocess import call

import click
from lztools.timing_and_dating import to_timespan

from lztools import networking
from lztools import work_logger
from lztools import zlick
from lztools.alarm import start_alarm

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@zlick.command()
@click.argument("BASE_IP")
def scan_network(base_ip):
    for ip in networking.scan_network(base_ip):
        print(ip)

@zlick.command()
@click.argument("time")
@click.option("-n", "--no-window", is_flag=True, default=False)
def alarm(time, no_window):
    """Alarm by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
    if no_window:
        start_alarm(to_timespan(time))
    else:
        call(["gnome-terminal", "--hide-menubar", "--geometry=40x8", "--", "alarm", time, "-n"])

@zlick.command(name="log-work")
def log_work():
    work_logger.log_work()

@zlick.command(name="parse-work")
def parse_work():
    work_logger.print_work()