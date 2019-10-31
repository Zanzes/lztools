import os

import click

from lztools import lzglobal, networking
from lztools import servers
from lztools import zlick

@zlick.command_matching_group()
@click.option('-v/-Q', '--verbose/--Quiet', default=False)
@click.option('-q', '--quiet', is_flag=True, default=False)
def sr(verbose:bool, quiet:bool):
    if verbose:
        quiet = False
    lzglobal.settings.set(verbose=verbose, quiet=quiet)

@sr.command()
# @click.argument("SEARCH_PATH", default=".")
# @click.option("-r/-c", "--recursive/--current-dir", default=False)
# @click.option("-n", "--name", default="_scatter_")
@click.option('-t', '--target')
def discover_servers(target:str):
    if target:
        server_list = servers.discover(target)
    else:
        server_list = servers.discover()
    servers.save(server_list)

@sr.command()
# @click.argument("SEARCH_PATH", default=".")
# @click.option("-r/-c", "--recursive/--current-dir", default=False)
@click.argument("NAME", default="")
@click.option("-i", "--ip")
def print_servers(name, ip):
    if os.sep == "/":
        os.system("clear")
    elif os.sep == "\\\\":
        os.system("cls")
    if not name and not ip:
        for server in servers.load():
            servers.print_details(server)
    else:
        if not name:
            server = servers.find(True, ip=ip)
        elif not ip:
            server = servers.find(True, custom_name=name)
        else:
            server = servers.find(True, ip=ip, custom_name=name)
        servers.print_details(server)

@sr.command()
@click.argument("NAME")
@click.option("-i", "--ip", is_flag=True, default=False, help="Use ip instead of name")
@click.option("-s", "--sudo", is_flag=True, default=False, help="Send 'sudo poweroff'")
def poweroff(name, ip, sudo:bool):
    if ip:
        server = servers.find(True, ip=name)
    else:
        server = servers.find(True, custom_name=name)
    if sudo:
        os.system(f"ssh {server.ip} sudo poweroff")
    else:
        os.system(f"ssh {server.ip} poweroff")

@sr.command()
@click.argument("NAME")
@click.option("-i", "--ip", is_flag=True, default=False, help="Use ip instead of name")
@click.option("-s", "--sudo", is_flag=True, default=False, help="Send 'sudo poweroff'")
def start_server(name, ip, sudo:bool):
    if ip:
        server = servers.find(True, ip=name)
    else:
        server = servers.find(True, custom_name=name)
    os.system(f"sudo etherwake -i {networking.find_network_card()} {server.mac}")