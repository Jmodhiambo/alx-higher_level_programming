#!/usr/bin/python3
"""
This module has:
    - Public instance method: def area(self).
    - Public instance method: def integer_validator(self, name, value)
"""


class BaseGeometry:
    """This is an empty class."""

    def area(self):
        """Raise an error with the message "area() is not implemented"."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
            - Raises TypeError if it is not an integer
            - Raises ValueError if it less than or equal to 0
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
