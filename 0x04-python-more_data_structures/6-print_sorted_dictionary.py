#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d1 = dict(sorted(a_dictionary.items()))
    for i in d1:
        print("{}: {}".format(i, d1[i]))
