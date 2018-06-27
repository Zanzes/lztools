import os

t = "python setup.py -V"

s = t.replace("    ", " ").replace("   ", " ").replace("  ", " ").replace(" ", " ").split(" ")

x = ""


for y in s:
    x += '"{}", '.format(y)
x = x.rstrip(", ")
os.system('echo \'{}\' | xclip -selection c'.format(x))
#print(x)
