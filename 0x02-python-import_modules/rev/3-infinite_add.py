#!/usr/bin/python3

import sys

if __name__ == "__main__":
    sum = 0
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0")
    else:
        for i in range(argc):
            sum += int(sys.argv[i + 1])
        print("{}".format(sum))
