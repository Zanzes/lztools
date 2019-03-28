import click
from zlick import command_matching_group

@command_matching_group()
@click.option("-v", "--verbose", is_flag=True, default=False)
def main(verbose):
    """Template bash command by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
    if verbose:
        print("Calling main functions")
    if verbose:
        print("Handling TEMPLATE_ARGUMENT")

if __name__ == '__main__':
    main()