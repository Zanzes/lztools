import click

from lztools import lzglobal
from lztools import zlick
from lztools import servers

@zlick.group()
@click.option('-v/-Q', '--verbose/--Quiet', default=False)
@click.option('-q', '--quiet', default=False)
def sr(verbose:bool, quiet:bool):
    if verbose:
        quiet = False
    lzglobal.settings.set(verbose=verbose, quiet=quiet)

@sr.command()
# @click.argument("SEARCH_PATH", default=".")
# @click.option("-r/-c", "--recursive/--current-dir", default=False)
# @click.option("-n", "--name", default="_scatter_")
def discover_servers():
    server_list = servers.discover()
    servers.save(server_list)

@sr.command()
# @click.argument("SEARCH_PATH", default=".")
# @click.option("-r/-c", "--recursive/--current-dir", default=False)
# @click.option("-n", "--name", default="_scatter_")
def print_servers():
    for server in servers.load():
        print("Server:")
        print(f"  IP: {server.ip}")
        print(f"  Name: {server.name}")
        print(f"  MAC: {server.mac}")
        print(f"  MName: {server.mac_name}")