#!  /usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

from PowerUtils.Managers import TempPath

def install_module(path, upload=False):
    with TempPath(path):
        subprocess.call(["python", "setup.py", "install"])
        if upload:
            subprocess.call(["twine", "upload", "dist/*"])
        subprocess.call(["rm", "-rf", "build"])
        subprocess.call(["rm", "-rf", "dist"])
        subprocess.call(["rm", "-rf", "*.egg-info"])







