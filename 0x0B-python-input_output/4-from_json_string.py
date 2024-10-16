#!/usr/bin/python3
"""
This module return an object from a JSON string.
"""


def from_json_string(my_str):
    """
    Return a Python object from a JSON string.
    """
    import json
    str_obj = json.loads(my_str)

    return (str_obj)
