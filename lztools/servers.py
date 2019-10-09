import os
from pathlib import Path
from typing import List

from lztools import bash, linux, windows
from lztools import lzglobal
from lztools import networking
from lztools.text import regex
from lztools.types import Server

_servers = None

def discover(target:str=None):
    if not lzglobal.settings.quiet:
        print("Searching for servers...")
    if not target:
        ip = "-sn "+str(networking.get_local_ip()).rsplit(".", 1)[0]+".*/24"
    else:
        ip = "-Pn "+target
    ip_list:str = bash.command(f"sudo nmap {ip} | tail -n +3 | head -n -1", return_result=True)
    ip_list = ip_list.split("Nmap scan report for ")
    servers = []
    for part in ip_list:
        server = Server()
        part = part.strip()
        lines = part.splitlines()
        if regex("\S* \([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}(\s|.)*MAC Address: [0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}", part, only_first=True, suppress=True):
            name, lines[0] = lines[0].split(" ", 1)
            server.system_name = name
        elif regex("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}(\s|.)*MAC Address: [0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}", part, only_first=True, suppress=True):
            pass
        else:
            continue
        server.ip = lines[0].strip("()")
        server.mac, mac_name = lines[2].split("Address: ", 1)[1].split(" ", 1)
        server.mac_name = mac_name.strip("()")
        if not lzglobal.settings.quiet:
            print(f"Discovered server at: {server.ip}")
        servers.append(server)

    return servers

def save(server_list: List[Server], skip_naming: bool = False, override=False):
    if not override:
        macs = [s.mac for s in server_list]
        existing = get_servers()
        for server in existing:
            if server.mac not in macs:
                server_list.append(server)

    with Path.home().joinpath(".lztools/servers").open("w") as f:
        for server in server_list:
            name_string = f"{server.ip}¤{server.system_name}¤{server.mac}¤{server.mac_name}"
            if not lzglobal.settings.quiet:
                print(f"Adding server {server.ip} ({server.system_name}):")
                if not skip_naming:
                    name_string = name_string + "¤" + input("Custom name: ") + os.linesep

            f.write(name_string)

def same(a:Server, b:Server):
    return a.ip == b.ip and a.custom_name == b.custom_name and a.mac == b.mac and a.mac_name == b.mac_name and a.system_name == b.system_name

def load() -> List[Server]:
    path = Path.home().joinpath(".lztools/servers")
    if not path.exists():
        path.touch(exist_ok=True)
    with path.open("r") as f:
        servers = []
        for line in f.readlines():
            server = Server()
            vals = line.strip().split("¤")
            if len(vals) > 4:
                server.ip, server.system_name, server.mac, server.mac_name, server.custom_name = vals
            else:
                vals.append(None)
                print(vals)
                server.ip, server.system_name, server.mac, server.mac_name, server.custom_name = vals
            servers.append(server)
    return servers

def find(like:bool=True, **kwargs) -> Server:
    for server in get_servers():
        for arg in kwargs:
            if like:
                if not kwargs[arg] in server.__dict__[arg]:
                    continue
            else:
                if not kwargs[arg] == server.__dict__[arg]:
                    continue
            return server

def print_details(server:Server, properties:List[str]=None ):
    if not properties:
        print("Server:")
        print(f"  IP:    {server.ip}")
        print(f"  Name:  {server.custom_name}")
        print(f"  MAC:   {server.mac}")
        print(f"  SName: {server.system_name}")
        print(f"  MName: {server.mac_name}")
        print()
    else:
        for prop in properties:
            print(f"{prop}: {server.__dict__[prop]}")

def get_servers() -> List[Server]:
    global _servers
    if not _servers:
        _servers = load()
    return _servers

def try_send_poweroff(server:Server, reboot:bool, sudo:bool):
    os.system(f"ssh {server.ip} '{linux.build_poweroff(reboot, sudo)}' 1> /dev/null 2> /dev/null")
    os.system(f"ssh {server.ip} '{windows.build_poweroff(reboot)}' 1> /dev/null 2> /dev/null")