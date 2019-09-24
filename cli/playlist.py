from pathlib import Path

import click

from lztools import zlick, playlist


@zlick.command_matching_group()
def main():
    """Tools to create, manage and convert M3U and XSPF playlists"""

@main.command()
@click.argument("NAME")
@click.argument("FILES", type=click.Path(exists=True, resolve_path=True), nargs=-1)
def create(name, files):
    if not files:
        si = click.get_text_stream("stdin").readlines()
        files = []
        for path in [Path(f.strip()) for f in si]:
            if path.exists():
                files.append(path)
            else:
                raise FileNotFoundError(path.absolute())
    else:
        f = []
        for file in files:
            f.append(Path(file))
        files = f
    playlist.create(Path(f"{name}.xspf"), files)