import zlick
import sh

import work_logger
from alarm import start_alarm, _to_timespan

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
gnome_terminal = sh.gnome_terminal.bake()

@zlick.command(context_settings=CONTEXT_SETTINGS)
@zlick.argument("time")
@zlick.option("-n", "--no-window", is_flag=True, default=False)
def alarm(time, no_window):
    """Alarm by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
    if no_window:
        start_alarm(_to_timespan(time))
    else:
        gnome_terminal("--hide-menubar", "--geometry=40x8", "--", "alarm", time, "-n")

@zlick.command(context_settings=CONTEXT_SETTINGS, name="log-work")
def log_work():
    work_logger.log_work()

@zlick.command(context_settings=CONTEXT_SETTINGS, name="parse-work")
def parse_work():
    work_logger.print_work()