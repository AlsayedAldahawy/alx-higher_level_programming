#!/usr/bin/python3

# Write a function that adds all unique integers in
# a list (only once for each integer).
# Prototype: def uniq_add(my_list=[]):
# You are not allowed to import any module

def uniq_add(my_list=[]):

    # 1- using loop
    sum = 0
    done = []
    for i in my_list:
        if i not in done:
            sum = sum + i
            done.append(i)
    return sum
