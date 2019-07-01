from pathlib import Path

import click

from lztools import io
from lztools import lzglobal
from lztools import zlick

@zlick.group()
@click.option('-v/-q', '--verbose/--quiet', default=False)
def scatter(verbose:bool):
    lzglobal.settings.set(verbose=verbose)

@scatter.command()
@click.argument("SEARCH_PATH", default=".")
@click.option("-r/-c", "--recursive/--current-dir", default=False)
@click.option("-n", "--name", default="_scatter_")
def now(search_path, recursive:bool, name:str):
    io.scatter_files(Path(search_path), recursive, scatter_name=name)

@scatter.command(name="print")
@click.argument("SEARCH_PATH", default=".")
@click.option("-r/-c", "--recursive/--current-dir", default=False)
@click.option("-n", "--name", default="_scatter_")
def print_s(search_path, recursive:bool, name:str):
    def print_scatter(p:Path):
        if p.name == name:
            print(p)
            text = p.read_text()
            for line in text.splitlines():
                print(f"    {line}")
    for _ in io.on_files(print_scatter, Path(search_path), subdirs=recursive):
        pass

@scatter.command()
@click.argument("COPY_FROM")
@click.argument("COPY_TO")
@click.option("-p", "--path", default=".")
@click.option("-n", "--name", default="_scatter_")
def add(copy_from, copy_to, path:str, name:str):
    p = Path(path)
    p = p.joinpath(name)
    if not p.exists():
        p.touch()
    text = p.read_text().splitlines()
    text.append(f"{copy_from} -> {copy_to}")
    p.write_text("\n".join(text))

@scatter.command()
@click.option("-p", "--path", default=".")
@click.option("-n", "--name", default="_scatter_")
def create(path:str, name:str):
    p = Path(path)
    if not p.name == name:
        p = p.joinpath(name)
    p.touch()