#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    answer = 0

    if operator == '+':
        answer = a + b
    elif operator == '-':
        answer = a - b
    elif operator == '*':
        answer = a * b
    elif operator == '/':
        answer = a / b
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, operator, b, answer))
