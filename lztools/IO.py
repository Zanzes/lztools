import subprocess

from lztools.ProDefered import define

define("xxa", lambda: "123")
define("xxb", lambda: "321")

def read_words_from_disk():
    return subprocess.check_output(["cat", "/usr/share/dict/words"]).splitlines()