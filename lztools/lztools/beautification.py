from lztools.lztools import command

def rainbow(text, frequency=0.1, hide_gap=True):
    if frequency is None:
        frequency = 0.1
    args = ["--freq", str(frequency)]

    m = "| sed '$d' " if hide_gap else ""
    argsd = str.join(" ", args)

    return command(f"echo \"{text}\" {m}| lolcat -f {argsd} 2> /dev/null", return_result=True)