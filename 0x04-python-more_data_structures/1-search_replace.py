#!/usr/bin/python3

# Write a function that replaces all occurrences of
# an element by another in a new list.
# Prototype: def search_replace(my_list, search, replace):
# my_list is the initial list
# search is the element to replace in the list
# replace is the new element
# You are not allowed to import any module


def search_replace(my_list, search, replace):

    # 1- using loops
    # new_list = []

    # for i in my_list:
    #     if i is search:
    #         i = replace
    #     new_list.append(i)

    # 2- using List Comprehensions
    # new_list = [i if i != search else replace for i in my_list]

    # 3- using lambda and map functions
    new_list = list(map(lambda x: x if x != search else replace, my_list))
    return new_list
