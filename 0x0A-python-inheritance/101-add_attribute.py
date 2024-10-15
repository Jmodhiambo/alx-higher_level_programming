#!/usr/bin/python3
"""
This module defines a function that adds a new attribute to an object
if it's possible.
"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible.
    Raises:
        TypeError: If the attribute can't be added to the object.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
