import os

import click

from lztools import lzglobal, networking, io, bash, xplatform, windows
from lztools import servers
from lztools import zlick
from lztools.enums import ClipboardBuffer
from lztools import linux


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

_remove_help_text = """Usage: sr SERVER remove [OPTIONS]

Options:
  --help  Show this message and exit.
  
Missing the SERVER argument."""

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
def remove():
    if not hasattr(lzglobal.settings, "server"):
        click.echo(_remove_help_text)
        quit()
    server = lzglobal.settings.server
    server_list = servers.get_servers()
    server_list.remove(server)
    servers.save(server_list, skip_naming=True, override=True)

@sr.command()
@click.option('-t', '--target')
def discover_servers(target:str):
    linux.require_apt_package("nmap")
    if target:
        server_list = servers.discover(target)
    else:
        server_list = servers.discover()
    servers.save(server_list, override=False)

@sr.command(name="print")
@click.argument("PROPERTIES", required=False, nargs=-1)
def my_print(properties):
    if os.sep == "/":
        os.system("clear")
    elif os.sep == "\\\\":
        os.system("cls")

    if not hasattr(lzglobal.settings, "server"):
        for server in servers.load():
            servers.print_details(server)
    else:
        if properties:
            servers.print_details(lzglobal.settings.server, properties=properties)
        else:
            servers.print_details(lzglobal.settings.server)

@sr.command()
@click.option("-s", "--sudo", is_flag=True, default=False, help="Execute as sudo")
@click.option("-r", "--reboot", is_flag=True, default=False, help="Reboot instead of shutting down")
@click.option("-b", "--blind-kill", is_flag=True, default=False, help="Try to poweroff a server without this software installed")
def poweroff(sudo:bool, reboot:bool, blind_kill:bool):
    if not hasattr(lzglobal.settings, "server"):
        print("")

    server = lzglobal.settings.server
    if not blind_kill:
        os.system(f"ssh {server.ip} 'server poweroff'")
    else:
        servers.try_send_poweroff(server, reboot, sudo)

@sr.command()
@click.option("-a", "--alternate", is_flag=True, default=False, help="Use etherwake instead of powerwake")
def start_server(alternate:bool):
    server = lzglobal.settings.server
    if alternate:
        os.system(f"sudo etherwake -i {networking.find_network_card()} {server.mac}")
    else:
        os.system(f"sudo powerwake {server.mac}")

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

@send.command()
@click.argument("VALUE", required=False)
@click.option("-c", "--clipboard", is_flag=True)
@click.option("-a", "--clipboard-alternate", is_flag=True)
def file(value, clipboard, clipboard_alternate):
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

