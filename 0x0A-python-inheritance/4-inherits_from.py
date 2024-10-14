#!/usr/bin/python3
"""
Checks if object is an isntance of a class directyly or indirectly
    - Returns True if true otherwise False
"""


def inherits_from(obj, a_class):
    """Checks if object is an instance of a class directyly or indirectly."""
    return isinstance(obj, a_class) and type(obj) is not a_class
