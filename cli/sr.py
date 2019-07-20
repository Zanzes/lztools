from pathlib import Path

import click

from lztools import io
from lztools import lzglobal
from lztools import zlick
from lztools import bash
from lztools import networking

@zlick.group()
@click.option('-v/-q', '--verbose/--quiet', default=False)
def sr(verbose:bool):
    lzglobal.settings.set(verbose=verbose)

@sr.command()
# @click.argument("SEARCH_PATH", default=".")
# @click.option("-r/-c", "--recursive/--current-dir", default=False)
# @click.option("-n", "--name", default="_scatter_")
def discover_servers():
    ip = str(networking.get_local_ip()).rsplit(".", 1)[0]+".*/24"
    bash.command(f"sudo nmap -sn {ip} | tail -n +3 | head -n -1")