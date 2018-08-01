#!  /usr/bin/env python
from functools import partial

from lztools.ColumnWriter import ColumnWriter
from lztools.Data.Images import get_random_image, search

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def a():
    time_operation(partial(search, "abcd", 1), 800, id="Find")
def b():
    time_operation(get_random_image, 800, id="Rand")

def pi(imgs):
    for img in imgs:
        print(img)

if __name__ == '__main__':
    # y = subprocess.check_output(["echo", "123"])
    # x = return_command_result("echo", "123\nass")
    # print(x)

    # w = BlockWriter()
    #
    # w.square_text("Joe sucks")
    # w.seperate()
    # w.write_text("tis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjaw\ntis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjawtis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjawtis ihdsaohw adp wapdwa poeigqwewqkeå kwqåwqoeåwqkldsak ldjaw")
    # w.seperate()
    # try:
    #     print(2 * "llo" / "a")
    # except Exception as e:
    #     w.split()
    #     w.seperate()
    #     exc_type, exc_value, exc_traceback = sys.exc_info()
    #     t = traceback.format_exception(exc_type, exc_value, exc_traceback)
    #     for x in t:
    #         w.write_text(x, colorizer=Ansi.red)
    #     w.seperate()
    # w.flush()

    cm = ColumnWriter()
    cm.mark_column("lol", "First", "X")
    cm.mark_column("lol2", "First", "X")
    cm.mark_column("lol", "Second", "X")
    print(cm.flush())

    # w = ColumnWriter(width=200)
    # w.add_mark("Joe", "First", "X")
    # w.add_mark("Joe", "Second", "X")
    # w.add_mark("Jack", "Second", "X")
    #
    # print(w.get_header())
    # for row in w.get_rows():
    #     print(row)




