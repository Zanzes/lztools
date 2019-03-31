from pathlib import Path

import click
from lztools import zlick
from lztools import pytools

@zlick.command_matching_group()
def main():
    """Python utilities by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""

@main.command()
@click.argument('name', type=click.Path())
@click.option("-p", "--parent", nargs=1, default="")
def create(name, parent):
    """Creates the template for a new pip package"""
    create(name, pack=parent)

@main.command()
@click.argument('paths', nargs=-1, type=click.Path())
@click.option("-u", "--upload", nargs=1, default=None)
@click.option("-a", is_flag=True, default=False, help="Adds 0.0.1 to version number")
@click.option("--add", default=None, type=str, help="Adds amount to version number (Default: 0.0.1)")
def install(paths, upload, a, add):
    """Installs one or more python3.7 modules and more by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙

    \b
    PATHS                   The path(s) to install modules from
                            \b
    --a                     Adds 0.0.1 to version number
                            \b
    --add X.X.X             Format: X.X.X where X is any integer
                            If no value is passed in the added amount defaults to 0.0.1
                            \b
                            Exampel 1: Default of 0.0.1 added
                            if original version is 0.0.0
                            lpy -a
                            the new version will be 0.0.1
                            \b
                            Exampel 2: 3.2.1 added
                            if original version is 1.2.3
                            lpy -a 3.2.1
                            the new version will be 4.4.4
                            \b
                            Exampel 3: 0.3.0 added and path specified
                            if original version is 3.0.3
                            lpy -a 0.3.0 path/to/module
                            the new version will be 1.2.3
                            \b
                            Exampel 4: Default of 0.0.1 added and path specified
                            if original version is 1.2.2
                            lpy path/to/module -a
                            the new version will be 1.2.3
                            \b
    -u, --upload PASSWORD   Uploads package using twine
    """
    if a or add is not None:
        if add is None:
            add = "0.0.1"

    should_upload = upload is not None

    if not paths:
        pytools.local_install(".", should_upload, add, upload)
    else:
        for x in paths:
            pytools.local_install(str(Path(x).absolute()), should_upload, add, upload)

@main.command()
@click.argument('path', type=click.Path(), default=".")
@click.option('-p', '--print-result', is_flag=True, default=False, help="Print the setup.py content instead of writing it to a file")
@click.option('-n', '--name', help="Set the name of the module")
def generate_setup(path, print_result, name):
    """Generates a setup.py file for a module"""
    mname = name if name else Path(path).absolute().name
    path = Path(path)
    if print_result:
        print(pytools.generate_setup(mname, path, write_to_file=False))
    else:
        pytools.generate_setup(mname, path)