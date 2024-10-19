#!/usr/bin/python3
"""
This module has a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    This function adds two intergers.
    Incase of either or both arguments are not interger or floats
        a TypeError is raised.
    Incase of floats they are converted to integers

    Args:
    a: The first value
    b: The second value (default is 98)

    Returns:
    The sum of a and b if both are integers.
    """
    if not isinstance(a, (int, float)) and isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) and isinstance(b, bool):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
