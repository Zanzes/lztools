from pathlib import Path
from typing import List

from lztools import bash
from lztools import lzglobal
from lztools import networking
from lztools.text import regex
from lztools.types import Server

def discover():
    if not lzglobal.settings.quiet:
        print("Searching for servers...")
    ip = str(networking.get_local_ip()).rsplit(".", 1)[0]+".*/24"
    ip_list:str = bash.command(f"sudo nmap -sn {ip} | tail -n +3 | head -n -1", return_result=True)
    ip_list = ip_list.split("Nmap scan report for ")
    servers = []
    for part in ip_list:
        server = Server()
        part = part.strip()
        lines = part.splitlines()
        if regex("\S* \([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}(\s|.)*MAC Address: [0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}:[0-9A-Z]{2}", part, only_first=True, suppress=True):
            name, lines[0] = lines[0].split(" ", 1)
            server.name = name
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

def save(server_list:List[Server]):
    servers = load()
    ips = [s.ip for s in servers]
    with open(Path.home().joinpath(".lztools/servers"), "a") as f:
        for server in server_list:
            if server.ip not in ips:
                if not lzglobal.settings.quiet:
                    print("Adding server")
                f.write(f"{server.ip}¤{server.name}¤{server.mac}¤{server.mac_name}\n")

def load():
    with open(Path.home().joinpath(".lztools/servers"), "r") as f:
        for line in f.readlines():
            server = Server()
            server.ip, server.name, server.mac, server.mac_name = line.split("¤")
            yield server