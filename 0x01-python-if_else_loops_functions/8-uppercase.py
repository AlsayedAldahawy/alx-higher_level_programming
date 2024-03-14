#!/usr/bin/python3

'''
Write a function that prints a string in uppercase followed by a new line.
'''


def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            i = chr(ord(i) - 32)

        print("{}".format(i), end=(""))
    print("".format())
