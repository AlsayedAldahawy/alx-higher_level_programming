#!/usr/bin/python3

'''
Write a program that prints the ASCII alphabet,
in lowercase, except q and e, not followed by a new line.
'''
for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    print("{}".format(chr(i)), end=(""))
