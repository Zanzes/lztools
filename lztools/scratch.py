from cli.lztools import fun
from click.testing import CliRunner

CliRunner().invoke(fun, input="jo jo")