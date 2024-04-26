#!/usr/bin/python3
""" Techniacl interview"""


def find_peak(list_of_integers):
    """function to get the peak number"""

    if not list_of_integers:
        return None

    # Initialize pointers for binary search
    left = 0
    right = len(list_of_integers) - 1

    # Binary search to find a peak
    while left < right:
        mid = (left + right) // 2
        # Check if mid is a peak
        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
