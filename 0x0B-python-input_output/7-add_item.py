#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list and then\
    saves them to a file.
"""


from sys import argv
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

args_lst = argv[1:]

for i in items:
    args_lst.append(i)

save_to_json_file(args_lst, "add_item.json")
