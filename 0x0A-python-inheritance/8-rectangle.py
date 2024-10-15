#!/usr/bin/python3
"""
This module has:
    - Class BaseGeometry
    - Class Rectangle
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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Inherits from class BaseGeometry."""
    def __init__(self, width, height):
        """Instanciates width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
