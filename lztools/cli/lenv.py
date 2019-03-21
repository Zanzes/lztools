import click
from core.click import command_matching_group
from cli import lzenv

@command_matching_group()
@click.option("-v", "--verbose", is_flag=True, default=False)
def main(verbose):
    """Template bash command by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
    if verbose:
        print("Calling main functions")
    lzenv.run()
    if verbose:
        print("Handling TEMPLATE_ARGUMENT")

if __name__ == '__main__':
    main()