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

    # Sort the dictionary by keys
    status_dict = {key: status_dict[key] for key in sorted(status_dict)}

    # Print the dictionary as pairs of <key>: <value>
    for key, value in zip(status_dict.keys(), status_dict.values()):
        print(f"{key}: {value}")


count = 0           # Initialize the lines counter
file_size = 0       # Initialize the file size
status_dict = {}    # Initialize an empty dictionary to handle status data

try:
    # To handle KeyboardInterrupt, we need to use exceptions

    # Read lines from stdin
    for line in sys.stdin:

        if count == 10:
            print_stats(file_size, status_dict)
            count = 0
        count += 1

        try:
            # If file size is not a valid value or does not exist, ignore
            file_size += int(line.split()[-1])
        except (IndexError, ValueError):
            pass

        try:
            # If status code is not a valid value or does not exist, ignore

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
