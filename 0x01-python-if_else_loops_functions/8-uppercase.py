#!/usr/bin/python3

'''
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()

'''


def uppercase(str):

    c = 0

    for i in str:
        if i >= 'a' and i <= 'z':
            c = ord(i) - 32
        else:
            c = ord(i)
        print("{}".format(chr(c)), end=(""))
    print("")
