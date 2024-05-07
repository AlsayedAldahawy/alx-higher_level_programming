#!/usr/bin/python3


'''
Module: 101-stats.py module
This module provides functions for processing log data and printing statistics.
'''

import sys


def print_stats(file_size, status_dict):
    '''
    Prints the total file size and a sorted list of status codes along with\
        their counts.

    Args:
        file_size (int): Total file size.
        status_dict (dict): Dictionary of status codes and their counts.

    Returns:
        None
    '''
    print("File size:", file_size)

    # Sorting the dictionary
    status_dict = {key: status_dict[key] for key in sorted(status_dict)}

    # print the dictionary as pairs of <key>: <value>
    for key, value in zip(status_dict.keys(), status_dict.values()):
        print(f"{key}: {value}")


count = 0           # Initialization of lines counter
file_size = 0       # Initialization of file_size to handle the file size
status_dict = {}    # Initialization of empty dict to handle the status data

try:
    # To handle the KeyboardInterrupt, we need to use exceptions

    # Taking lines from the stdin
    for line in sys.stdin:

        if count == 10:
            print_stats(file_size, status_dict)
            count = 0
        count += 1

        try:
            # If file size is not a valid value or not exist, pass
            file_size += int(line.split()[-1])
        except (IndexError, ValueError):
            pass

        try:
            # If status_code is not a valid value or not exist, pass
            status_code = int(line.split()[-2])
            if status_code not in status_dict:
                status_dict[status_code] = 1
            else:
                status_dict[status_code] += 1
        except (ValueError, IndexError):
            pass

    print_stats(file_size, status_dict)

except KeyboardInterrupt:
    print_stats(file_size, status_dict)
    raise
