import re

def regex(expr, text, only_first=False, suppress=False):
    if only_first:
        if suppress:
            try:
                return re.search(expr, text).group(0)
            except:
                pass
        else:
            return re.search(expr, text).group(0)
    else:
        return (x for x in re.findall(expr, text))

def extract_module_version(text):
    return regex(" \d+\.\d+\.\d+", text, only_first=True)[1:]