#!/usr/bin/python3
"""
This module writes an Object to a text file, using a JSON representation."
"""


def save_to_json_file(my_obj, filename):
    """
    This function writes an Object to a text file, using a JSON representation.
    """
    import json
    to_json = json.dumps(my_obj)

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(to_json)
