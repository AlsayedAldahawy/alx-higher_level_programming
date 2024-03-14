#!/usr/bin/python3

'''
    Write a program that prints the ASCII alphabet,
    in reverse order, alternating lowercase and uppercase
    (z in lowercase and Y in uppercase)
'''

for i in range(122, 96, -1):
    if i % 2 == 0:
        c = chr(i)
    else:
        c = chr(i - 32)
    print(c, end=(""))
