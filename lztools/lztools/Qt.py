from pathlib import Path

def generate(path):
    path = Path(path)
    for p in path.iterdir():
        print(p)