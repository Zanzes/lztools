from cli.lztools import to_art

from lztools import Images
from lztools.sound import beep, beep_on_off

from lztools.text import print_dict, print_dir_values, print_collection

i = Images.get_random_image(count=2)
for x in i:
    print(x)

    print(to_art(x, 50, True))
