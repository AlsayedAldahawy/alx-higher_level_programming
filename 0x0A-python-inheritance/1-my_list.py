#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    '''
        class inherit from list object
        it has method: print_sorted that prints the list, but sorted.
    '''

    def print_sorted(self):
        '''
            prints the list sorted (ascending sort)
        '''
        print(sorted(self))
