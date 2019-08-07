import os
from pathlib import Path
from typing import List

from lztools import bash
from lztools import lzglobal
from lztools import networking
from lztools.text import regex
from lztools.types import Server


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

def save(server_list:List[Server], skip_naming:bool=False):
    servers = load()
    ips = [s.ip for s in servers]
    with open(Path.home().joinpath(".lztools/servers"), "a") as f:
        for server in server_list:
            if server.ip not in ips:
                name_string = f"{server.ip}¤{server.system_name}¤{server.mac}¤{server.mac_name}"
                if not lzglobal.settings.quiet:
                    print(f"Adding server {server.ip} ({server.system_name}):")
                    if not skip_naming:
                        name_string = name_string + "¤" + input("Custom name: ") + os.linesep
                f.write(name_string)

def load() -> List[Server]:
    path = Path.home().joinpath(".lztools/servers")
    if not path.exists():
        path.touch(exist_ok=True)
    with open(path, "r") as f:
        for line in f.readlines():
            server = Server()
            vals = line.strip().split("¤")
            if len(vals) > 4:
                server.ip, server.system_name, server.mac, server.mac_name, server.custom_name = vals
            else:
                vals.append(None)
                server.ip, server.system_name, server.mac, server.mac_name, server.custom_name = vals
            yield server

live_servers = load()

def find(like:bool=True, **kwargs) -> Server:
    for server in live_servers:
        for arg in kwargs:
            if like:
                if not kwargs[arg] in server.__dict__[arg]:
                    continue
            else:
                if not kwargs[arg] == server.__dict__[arg]:
                    continue
            return server

def print_details(server):
    print("Server:")
    print(f"  IP:    {server.ip}")
    print(f"  Name:  {server.custom_name}")
    print(f"  MAC:   {server.mac}")
    print(f"  SName: {server.system_name}")
    print(f"  MName: {server.mac_name}")
    print()



