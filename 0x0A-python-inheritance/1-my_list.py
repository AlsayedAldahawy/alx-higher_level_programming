#!/usr/bin/python3

'''
Module contains MyList class
'''


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    This class extends the functionality of the list class by adding a\
        new method, `print_sorted()`,
    which prints the elements of the list in sorted order.

    Example:
        >>> my_custom_list = MyList([3, 1, 2])
        >>> my_custom_list.print_sorted()
        [1, 2, 3]
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.

        Example:
            >>> my_custom_list = MyList([3, 1, 2])
            >>> my_custom_list.print_sorted()
            [1, 2, 3]
        """
        print(sorted(self))
