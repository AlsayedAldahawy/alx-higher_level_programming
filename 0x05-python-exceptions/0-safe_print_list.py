#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    return_value = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
            return_value += 1

        except IndexError:
            break
    print("")
    return return_value
