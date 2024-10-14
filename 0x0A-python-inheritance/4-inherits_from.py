#!/usr/bin/python3
"""
This module checks if object is an isntance of a class whether inherited or directly
    - Returns True if true otherwise False
"""


def inherits_from(obj, a_class):
    """Checks if object is an isntance of a class whether inherited or directly."""
    return isinstance(obj, a_class) and type(obj) is not a_class
