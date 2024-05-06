#!/usr/bin/python3
"""
Appends a new string after a specified search string in a text file.

Args:
    filename (str): The name of the file to modify.
    search_string (str): The string to search for in each line of the file.
    new_string (str): The string to append after the search string.

Example:
    Suppose we have a file named "my_file.txt" with the following content:
    ```
    Line 1: Hello, world!
    Line 2: This is a test.
    Line 3: Goodbye, world!
    ```

    We can use the `append_after` function as follows:
    ```
    append_after(filename="my_file.txt", search_string="This is a test.",\
        new_string="Inserted line.")
    ```

    After execution, the file will be updated as:
    ```
    Line 1: Hello, world!
    Line 2: This is a test.
    Inserted line.
    Line 3: Goodbye, world!
    ```
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a new string after a specified search string in a text file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line of the file.
        new_string (str): The string to append after the search string.
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    i = 1
    for line in lines:
        if search_string in line:
            lines.insert(i, new_string + "\n")
        i += 1

    with open(filename, "w") as file:
        file.writelines(lines)
