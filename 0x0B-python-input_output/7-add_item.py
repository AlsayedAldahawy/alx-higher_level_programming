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
except Exception:
    items = []

items += argv[1:]


save_to_json_file(items, "add_item.json")
