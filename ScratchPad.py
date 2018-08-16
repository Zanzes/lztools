#!  /usr/bin/env python3.7
from lztools.git import list_files, load_file, save_file

i = input("0 = List(Default), 1 = Load, 2 = Save:\n")
files = list(list_files("/home/zanzes/dev/resources"))

if i == "1":
    for k, v in enumerate(files):
        print(f'{k}:\t{v.path}')
    id = int(input("File #:\n"))
    load_file("/home/zanzes/dev/resources", files[id])

elif i == "2":
    file = input("file: ")
    save_file("/home/zanzes/dev/resources", file)
else:
    for k, v in enumerate(files):
        print(f'{k}:\t{v.path}')


