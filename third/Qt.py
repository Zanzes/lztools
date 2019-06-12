import importlib
import os
import re
import subprocess
from pathlib import Path

import sys
from PyQt5.QtWidgets import QApplication

def _import_pyui(path:Path):
    name = pathing.name(path)
    module = importlib.machinery.SourceFileLoader(name, str(path)).load_module()
    return module

def _generate(path:Path):
    if path.name.endswith(".ui"):
        np = Path(str(path).rsplit(".ui", 1)[0] + ".py")
        print(f"Generating: {path} -> {np}")
        if not np.parent.exists():
            np.parent.mkdir(parents=True, exist_ok=True)
        elif np.exists():
            np.unlink()
        text = path.read_text()
        rp = re.search("<include location=\".*", text).group()
        text = text.replace(rp, f"<include location=\"{resources_path}{os.path.sep}resources.qrc\"/>")
        path.write_text(text)
        out = subprocess.getoutput(f"pyuic5 {path}")
        out = out.replace("import resources_rc", "import MiRResources.resources_rc")
        np.write_text(out)
        return _import_pyui(np)

def generate_pyui(path:Path):
    collections.exhaust(on_files(_generate, path))

def run_view(view):
    app = QApplication(sys.argv)
    win = view()
    win.show()
    sys.exit(app.exec())