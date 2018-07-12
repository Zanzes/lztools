#!  /usr/bin/env python
import progressbar
import time

import sys

for i in progressbar.progressbar(range(100), redirect_stdout=True, redirect_stderr=True):
    print(i, file=sys.stderr)
    time.sleep(0.1)