#!/usr/bin/python3
"""
This module (3-is_kind_of_class):
    - Returns True if the object is an instance or an instance of a class
    - Otherwise returns False
"""


def is_kind_of_class(obj, a_class):
    """Checks is an object is an instance or instance of a class."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
