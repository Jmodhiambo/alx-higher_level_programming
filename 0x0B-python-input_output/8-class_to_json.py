#!/usr/bin/python3
"""
This module provides a function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization.
    """
    return obj.__dict__
