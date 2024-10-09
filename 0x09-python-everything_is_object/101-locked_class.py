#!/usr/bin/python3
"""
This module defines a class `LockedClass` that restricts the creation of
instance attributes to only `first_name`. Any attempt to create other
instance attributes dynamically will raise an `AttributeError`.
"""


class LockedClass:
    """
    A class that only allows dynamic creation of an instance attribute
    called 'first_name'. Any attempt to create other attributes
    will result in an AttributeError.
    """
    __slots__ = ['first_name']
