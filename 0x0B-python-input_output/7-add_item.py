#!/usr/bin/python3
"""
This module adds all arguments to a Python list,
     and then save them to a file.
"""

import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """The main function."""
    args = []
    args = argv[1:]
    if len(args) <= 0:
        return

    filename = "add_item.json"
    save_to_json_file(args, filename)
    load_from_json_file(filename)


main()
