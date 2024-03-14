#!/usr/bin/python3

'''
Write a function that prints the last digit of a number.
Returns the value of the last digit
'''


def print_last_digit(number):
    print("{}".format(abs(number) % 10), end=(""))
    return (abs(number) % 10)
