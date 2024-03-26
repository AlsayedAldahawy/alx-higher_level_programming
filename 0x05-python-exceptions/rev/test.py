#!/usr/bin/python3
try:
    amount = 1999
    if amount >= 2999:
        raise ValueError("Please add money in your account")
    else:
        print("You are eligible to purchase DSA Self Paced course")
except ValueError as h:
    print(h)
