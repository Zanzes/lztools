import click
from lztools.zlick import command_matching_group
from window import template

@proper_group()
@click.argument("TEMPLATE_ARGUMENT", default=click.get_text_stream('stdin'))
@click.option("-v", "--verbose", is_flag=True, default=False)
def main(template_argument, verbose):
    """Template bash command by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
    if verbose:
        print("Calling main functions")
    template()
    if verbose:
        print("Handling TEMPLATE_ARGUMENT")
    if template_argument:
        print(f"TEMPLATE_ARGUMENT: {template_argument}")