#!/usr/bin/python3
"""
This module creates an Object form a "JSON file".
"""

import json


def load_from_json_file(filename):
    """This function that creates an Object from a “JSON file”."""
    with open(filename, mode="r", encoding="utf-8") as f:
        json.load(f)
