#!/usr/bin/python3

''' Function that writes a string to a text file (UTF-8) and returns the
         number of characters written:'''


def write_file(filename="", text=""):
    """
    Writes the specified text to the given file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.

    Example:
        >>> write_file("output.txt", "Hello, world!")
        13
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
