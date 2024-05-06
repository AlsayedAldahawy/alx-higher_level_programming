#!/usr/bin/python3

''' Function that reads a text file (UTF-8) and prints its content to stdout'''


def read_file(filename=""):
    """
    Reads the specified text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.

    Example:
        >>> read_file("sample.txt")
        This is the content of the sample file.
        Hello, world!
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
