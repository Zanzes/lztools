#!/usr/bin/python3.7
import os
from pathlib import Path
import remote_tools
from lztools import servers
from lztools.enums import RemoteTool
from lztools.types import Server

print("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤    DEBUGGING    ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")

def execute_on(execute, server:Server):
    tool_path = Path(remote_tools.__path__[0]).joinpath(execute+".py")
    if not tool_path.exists():
        raise FileNotFoundError(str(tool_path))
    cmd = f"cat '{tool_path.absolute()}' | ssh {server.ip} python3 -"
    print(cmd)
    os.system(cmd)

s = servers.find(True, custom_name="rasp")
execute_on(RemoteTool.IdentifyOS, s)