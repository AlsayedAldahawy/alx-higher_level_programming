#!/usr/bin/python3

""" Function that appends a string at the end of a text file (UTF-8) and returns\
        the number of characters added:"""

def append_write(filename="", text=""):
    """
    Appends the specified text to the given file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.

    Example:
        >>> append_write("output.txt", "Hello, world!")
        13
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
