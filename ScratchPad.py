import os

path = os.path.dirname(os.path.realpath(__file__))

print os.getcwd()
print path

os.chdir(path)

print os.getcwd()

import target

print target.x

with open("target.txt", "r+") as f:
    print f.readlines()

