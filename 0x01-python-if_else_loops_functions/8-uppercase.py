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

    for i in str:
        if i >= 'a' and i <= 'z':
            i = chr(ord(i) - 32)

        print("{}".format(i), end=(""))
    print("".format())
