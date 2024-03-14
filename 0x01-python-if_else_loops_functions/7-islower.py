#!/usr/bin/python3

'''
Prototype: def islower(c):
Returns True if c is lowercase
Returns False otherwise
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()

'''


def islower(c):

    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
