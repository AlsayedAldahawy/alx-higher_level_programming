#!/usr/bin/python3
def separate_characters_on_lines(input_string):
    result = ""
    for char in input_string:
        result += char + "\n"
    return result[:-1]

input_text = "Hello, World!"
output_text = separate_characters_on_lines(input_text)
print(output_text)
