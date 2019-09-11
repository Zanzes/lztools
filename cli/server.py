import os

import click

from lztools import lzglobal, networking, io, bash
from lztools import servers
from lztools import zlick
from lztools.enums import ClipboardBuffer


class OptArgGroup(zlick.CommandMatchingGroup):
    def parse_args(self, ctx, args):
        if args:
            if args[0] not in ["self", ".", "me", "none", "-", "_"]:
                server = servers.find(True, custom_name=args[0])
                if server:
                    lzglobal.settings.set(server=server)
                else:
                    args.insert(0, '')
            else:
                args.insert(0, '')
        super(OptArgGroup, self).parse_args(ctx, args)

# noinspection PyUnusedLocal
@click.group(cls=OptArgGroup)
@click.argument("SERVER", default="")
@click.option("-i", "--ip", is_flag=True, default=False, help="Use ip instead of name")
@click.option('-v/-Q', '--verbose/--Quiet', default=False)
@click.option('-q', '--quiet', is_flag=True, default=False)
def sr(server, ip, verbose:bool, quiet:bool):
    """Server tools

    SERVER: if no server needs to be specified one
            following can be passed in instead:
                self . me none - _ """
    if verbose:
        quiet = False
    lzglobal.settings.set(verbose=verbose, quiet=quiet)

@sr.command()
@click.option('-t', '--target')
def discover_servers(target:str):
    if target:
        server_list = servers.discover(target)
    else:
        server_list = servers.discover()
    servers.save(server_list)

@sr.command()
def print_servers():
    if os.sep == "/":
        os.system("clear")
    elif os.sep == "\\\\":
        os.system("cls")

    if not hasattr(lzglobal.settings, "server"):
        for server in servers.load():
            servers.print_details(server)
    else:
        servers.print_details(lzglobal.settings.server)

@sr.command()
@click.option("-s", "--sudo", is_flag=True, default=False, help="Send 'sudo poweroff'")
def poweroff(sudo:bool):
    server = lzglobal.settings.server
    if sudo:
        os.system(f"ssh {server.ip} sudo poweroff")
    else:
        os.system(f"ssh {server.ip} poweroff")

@sr.command()
def start_server():
    server = lzglobal.settings.server
    os.system(f"sudo etherwake -i {networking.find_network_card()} {server.mac}")

@sr.command()
def connect():
    server = lzglobal.settings.server
    os.system(f"ssh -XC {server.ip}")

@sr.command()
@click.argument("VALUE", required=False)
@click.option("-c", "--clipboard", is_flag=True)
@click.option("-a", "--clipboard-alternate", is_flag=True)
def play(value, clipboard, clipboard_alternate):
    """Play item in vlc"""
    if not value and not clipboard and not clipboard_alternate:
        value = input()
    elif clipboard:
        value = bash.get_clipboard_content(ClipboardBuffer.clipboard)
    elif clipboard_alternate:
        value = bash.get_clipboard_content(ClipboardBuffer.primary)
    os.system(f"notify-send 'Playing' '{value}'")

    server = lzglobal.settings.server

    os.system(f"ssh -XC {server.ip} 'export DISPLAY=:0;vlc --one-instance \"{value}\" &' 1> /dev/null 2> /dev/null")

@sr.group(cls=zlick.CommandMatchingGroup)
def send():
    pass

@send.command()
@click.argument("VALUE", required=False)
@click.option("-c", "--clipboard", is_flag=True)
@click.option("-a", "--clipboard-alternate", is_flag=True)
def text(value, clipboard, clipboard_alternate):
    if not value and not clipboard and not clipboard_alternate:
        value = input()
    elif clipboard:
        value = bash.get_clipboard_content(ClipboardBuffer.clipboard)
    elif clipboard_alternate:
        value = bash.get_clipboard_content(ClipboardBuffer.primary)

    os.system(f"notify-send 'Sending' '{value}'")

    server = lzglobal.settings.server

    tmp_file = io.get_temporary_file()
    tmp_file.write_text(value + os.linesep)

    os.system(f"cat {tmp_file.absolute()} | ssh {server.ip} 'cat >> shared-text'")

