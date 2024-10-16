#!/usr/bin/python3
"""
This module adds all arguments to a Python list,
     and then saves them to a file.
"""

import json
import os
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """The main function."""
    filename = "add_item.json"

    """Try to load the existing list from the file."""
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    """Append new arguments to the list."""
    my_list.extend(argv[1:])

    """Save the updated list back to the file."""
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
