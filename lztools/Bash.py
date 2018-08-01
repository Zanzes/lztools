from subprocess import check_output, Popen, run

import os

def command_result(name, *args):
    try:
        result = run([name, *args], capture_output=True, check=True, universal_newlines=True, encoding="utf8")
        # x = check_output([name, *args], universal_newlines=True)
        #
        # Popen()
        return result.stderr, result.stdout
    except:
        pass

# def command(command):
#     os.system(command)

def command(command, *args):
    fargs = " ".join(args)
    os.system(f"{command} {fargs}")

def apt_install(package):
    command(f"sudo apt install -y {package}")


def load_words():
    res = command_result("cat", "/usr/share/dict/words")
    return res
