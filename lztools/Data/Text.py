import random
import re

from lztools.DataTypes.LazyVariable import super_property
from lztools.IO import read_words_from_disk

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

words = super_property(read_words_from_disk)

# def get_all_words():
#     global words
#     if words is None:
#         words = read_words_from_disk()
#     return words

def get_random_word():
    return random.choice(words)