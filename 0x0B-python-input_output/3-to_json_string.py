#!/usr/bin/python3
"""
This module returns the JSON representation of an object (string).
"""


def to_json_string(my_obj):
    """Converts a string to JSON repr. of object."""
    import json
    json_repr = json.dumps(my_obj)

    return (json_repr)
