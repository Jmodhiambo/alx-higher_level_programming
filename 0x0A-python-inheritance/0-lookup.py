#!/usr/bin/python3
"""
Module 0-lookup
   -Returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """Returns a list of available attributes an methods of an object."""
    return dir(obj)
