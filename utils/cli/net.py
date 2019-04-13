import click

from lztools import networking

@click.command()
@click.argument('IP', type=str, default="192.168.87.1")
def main(ip):
    res = networking.scan_network(ip)
    for x in res:
        print(x)