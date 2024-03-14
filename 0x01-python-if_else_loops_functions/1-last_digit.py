#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = -number % 10
else:
    last_digit = number % 10

if last_digit > 5:
    str_ = "and is greater than 5"
elif last_digit < 6:
    str_ = "and is less than 6 and not 0"
else:
    str_ = "and is 0"

print(f"Last digit of {number} is {abs(last_digit)} and {str_}")
