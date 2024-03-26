#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
            if i + 1 == x or my_list[i] == my_list[-1]:
                print("")
                break

    except ValueError:
        pass
    return i + 1
