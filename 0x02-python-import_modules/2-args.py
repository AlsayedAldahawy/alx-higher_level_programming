#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
    else:
        print("{} arguments:".format(len(argv) - 1))
    i = 1
    while i < len(argv):
        print("{}: {}".format(i, argv[i]))
        i = i + 1
