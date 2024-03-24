#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # 1- using loops
    # newList = []
    # for i in set_1:
    #     if i not in set_2:
    #         newList.append(i)
    # for i in set_2:
    #     if i not in set_1:
    #         newList.append(i)
    # return newList

    # 2- using set operations (&, |, -, ^)
    return (set_1 | set_2) - (set_1 & set_2)
