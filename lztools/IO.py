import subprocess


def read_words_from_disk():
    return subprocess.check_output(["cat", "/usr/share/dict/words"]).splitlines()