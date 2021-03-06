import subprocess
from pathlib import Path

from lztools import constants
from lztools.lztext import lztext
from lztools.linux.bash import command

def read_bash_rc() -> str:
    return subprocess.getoutput("cat $HOME/.bashrc")

def get_section_names():
    for line in read_bash_rc().strip().splitlines():
        if line.endswith(" " + constants.RC_SECTION_START_RIGHT):
            line = line.replace(" " + constants.RC_SECTION_START_RIGHT, "")
            line = line.replace(constants.RC_SECTION_START_LEFT + " ", "")
            yield line

def get_section(name, include_padding):
    rcdata = read_bash_rc()
    taken = rcdata.split(f"{constants.RC_SECTION_START_LEFT} {name} {constants.RC_SECTION_START_RIGHT}", 1)[1]
    taken = taken.split(f"{constants.RC_SECTION_END_LEFT} {name} {constants.RC_SECTION_END_RIGHT}", 1)[0]
    if include_padding:
        taken = f"""# {constants.RC_SECTION_START_LEFT} {name} {constants.RC_SECTION_START_RIGHT}
{taken}
{constants.RC_SECTION_END_LEFT} {name} {constants.RC_SECTION_END_RIGHT}"""
    return taken

def get_history():
    return command("cat", "{}/.bash_history".format(str(Path.home())), return_result=True)

def search_history(term, regex=False):
    if not regex:
        for line in get_history().splitlines():
            if term in line:
                yield line
    else:
        return lztext.regex(term, get_history())

# bashrc_symbols = {
#     "customSection": "# ▂▃▅▇█▓▒░LAZ░▒▓█▇▅▃▂",
#     "aliasStart": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> ALIAS START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
#     "aliasEnd": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> ALIAS END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
#     "exportStart": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> EXPORT START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
#     "exportEnd": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> EXPORT END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
#     "variablesStart": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> VARIABLES START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
#     "variablesEnd": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> VARIABLES END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
#     "otherStart": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> OTHER START <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙",
#     "otherEnd": "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> OTHER END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙"
# }

# def apt_install(package):
#     command(f"sudo apt install -y {package}")
#
# def get_bashrc_path() -> str:
#     return f"{str(Path.home())}/.bashrc"
#
# def get_bashrc_other_path() -> str:
#     return f"{lztools.__path__[0]}/lzresources/bashrc"
#
# def get_bashrc() -> str:
#     return command("cat", get_bashrc_path(), return_result=True)
#
# def get_bashrc_other() -> str:
#     other_path = get_bashrc_other_path()
#     return command("cat", other_path, True)
#
# def _rcadd(lztext, symbol):
#     start, end = get_bashrc().split(symbol, 1)
#     start = start + lztext
#     end = symbol + end
#     return f"{start}\n{end}"
#
# def _rccopy(rc, replacement, symbol):
#     start, _ = rc.split(symbol, 1)
#     _, replacement = replacement.split(symbol, 1)
#     return start[:-1] + symbol + replacement
#
# def add_bashrc_alias(lztext):
#     print(_rcadd(lztext, bashrc_symbols["aliasEnd"]), end="")
#
# def add_bashrc_variabel(lztext):
#     print(_rcadd(lztext, bashrc_symbols["variablesEnd"]), end="")
#
# def add_bashrc_export(lztext):
#     print(_rcadd(lztext, bashrc_symbols["exportEnd"]), end="")
#
# def add_bashrc_other(lztext):
#     print(_rcadd(lztext, bashrc_symbols["otherEnd"]), end="")
#
# def copy_bashrc_other(to_me:bool=True, out_path:str=None):
#     if to_me:
#         old = get_bashrc()
#         new = get_bashrc_other()
#         path = get_bashrc_path()
#     else:
#         old = get_bashrc_other()
#         new = get_bashrc()
#         path = get_bashrc_other_path()
#
#     if out_path is not None:
#         path = out_path
#
#     new_rc = _rccopy(rc=old, replacement=new, symbol=bashrc_symbols["customSection"])
#
#     with open(path, "w") as f:
#         f.write(new_rc)
#
# def delete_items_in_dir(path:str):
#     if Path(path).is_dir():
#         command(["rm", "-rf", f"{path.rstrip('/*')}/*"])
#     else:
#         raise NotADirectoryError(path)
#
# def get_wifi_network_name():
#     res:str = command("iwgetid", return_result=True)
#     return res.split('"', 1)[1].rsplit('"')[0]