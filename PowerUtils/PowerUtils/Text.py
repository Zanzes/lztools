import re

def regex(expr, text, first=False, suppress=False):
    if first:
        if suppress:
            try:
                yield re.search(expr, text).group(0)
            except:
                pass
        else:
            yield re.search(expr, text).group(0)
    else:
        for x in re.findall(expr, text):
            yield x