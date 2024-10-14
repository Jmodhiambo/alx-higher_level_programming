#!/usr/bin/python3
"""
This module try to find if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Checks if an object belongs to a particular class."""
    return type(obj) is a_class
