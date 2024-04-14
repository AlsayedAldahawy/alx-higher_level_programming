#!/usr/bin/python3

'''
    module includes text_identation function
'''


def text_indentation(text):
    """
    Prints the provided text with 2 new lines after each occurrence
        of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If `text` is not a string.

    Example:
        >>> text_indentation("Hello. How are you? I'm fine.")
        Hello
        How are you
        I'm fine.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
            while i + 1 < len(text) and text[i + 1] in [' ', '\n']:
                i += 1
        i += 1
