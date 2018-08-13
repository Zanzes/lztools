import getpass
import shlex
from pathlib import Path
from subprocess import call

def is_initializd():
    return Path("/opt/lztools").exists()

def initialize(override_existing=False):
    if override_existing or not is_initializd():
        home = Path.home().resolve()
        tp = home.joinpath(".lztools")
        rcp = home.joinpath(".bashrc")

        tp.mkdir(exist_ok=True)
        call(["sudo", "rm", "-rf", str(tp)+"/*"])
        res = tp.joinpath("resources").resolve()
        res.mkdir()
        res.joinpath("sourcing").touch()

        data = ""
        with open(str(rcp), "r") as f:
            data = f.readline()
        if "PROMPT_COMMAND" not in data:
            marker = "# ∙∙∙∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ☼)===> OTHER END <===(☼ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙∙∙∙"
            with open(str(rcp), "w") as f:
                data = data.replace(f"\n\n{marker}", f"PROMPT_COMMAND='source {str(tp)}/resources/sourcing'\n\n{marker}")
                f.write(data)




