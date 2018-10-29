import click
import sh

from lztools.extras import work_logger
from lztools.extras.alarm import run_timer, to_timespan

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
gnome_terminal = sh.gnome_terminal.bake()

@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("time")
@click.option("-n", "--no-window", is_flag=True, default=False)
def alarm(time, no_window):
    """Alarm by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
    if no_window:
        run_timer(to_timespan(time))
    else:
        gnome_terminal("--hide-menubar", "--geometry=40x8", "--", "alarm", time, "-n")

@click.command(context_settings=CONTEXT_SETTINGS)
def log_work():
    work_logger.work_logger()

@click.command(context_settings=CONTEXT_SETTINGS)
def parse_work():
    work_logger.work_interpreter()