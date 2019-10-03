from pathlib import Path
from typing import List


def get_files(path:Path) -> List[Path]:
    if path.is_file():
        yield from [path]
        return
    for file in path.iterdir():
        if file.is_file():
            yield file
        elif file.is_dir():
            yield from get_files(file)

def create(playlist:Path, files:List[Path]):
    if not playlist.exists():
        playlist.touch()
    with playlist.open("w") as f:
        f.write("""<?xml version="1.0" encoding="UTF-8"?>
<playlist version="1" xmlns="http://xspf.org/ns/0/">
  <trackList>
""")
        for path in files:
            for file in get_files(path):
                f.write(f"""    <track><location>file://{file.absolute()}</location></track>
""")
        f.write("""  </trackList>
</playlist>""")