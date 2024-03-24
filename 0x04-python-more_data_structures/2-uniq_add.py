#!/usr/bin/python3

# Write a function that adds all unique integers in
# a list (only once for each integer).
# Prototype: def uniq_add(my_list=[]):
# You are not allowed to import any module

def uniq_add(my_list=[]):

    sum = 0
    # 1- first method
    # uniqe = []
    # for i in my_list:
    #     if i not in uniqe:
    #         sum = sum + i
    #         uniqe.append(i)

    # 2- using set()

    set(my_list)
    for i in set(my_list):
        sum = sum + i
    return sum
