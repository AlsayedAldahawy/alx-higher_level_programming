#!/usr/bin/python3
def common_elements(set_1, set_2):
    # 1- using loops

    # newList = []
    # for i in set_1:
    #     if i in set_2:
    #         newList.append(i)
    # return newList

    # 2- using set operations (&, |, -, +, ^)
    return set_1 & set_2
