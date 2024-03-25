#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    # 1- using comprehension
    new_dictionary = {key: value * 2 for key, value in a_dictionary.items()}

    # 2- using loop
    # new_dictionary = {}
    # for key, value in a_dictionary.items():
    #     new_dictionary[key] = value * 2
    return new_dictionary
