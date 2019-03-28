import zlick
from zlick import proper_group

@proper_group()
@zlick.argument("TEMPLATE_ARGUMENT", default=zlick.get_text_stream('stdin'))
@zlick.option("-v", "--verbose", is_flag=True, default=False)
def main(template_argument, verbose):
    """Template bash command by Laz, ᒪᗩᘔ, ㄥ卂乙, ןɐz, lคz, ℓДՀ, լᕱᏃ, Նคઽ, ﾚﾑ乙"""
    if verbose:
        print("Calling main functions")
    print("Work")
    if verbose:
        print("Handling TEMPLATE_ARGUMENT")
    if template_argument:
        print(f"TEMPLATE_ARGUMENT: {template_argument}")