from os import getcwd
from pathlib import Path

print(getcwd())
for x in Path(".").glob("*egg*"):
