from cli.lztools import to_art

from lztools import Images
from lztools.beautification import rainbow

i = Images.get_random_image(count=2)
for x in i:
    print(x)

    print(rainbow(to_art(x, 50, True)))
