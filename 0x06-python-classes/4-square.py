#!/usr/bin/python3
"""
Module 4-square
This module defines a class Square by:
    - Private instance attribute: size
    - Property getter and setter for size
    - Public method: area
"""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """
        Initializes the square.
        Ensures size is an integer and >= 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size.
        Ensures size is an integer and >= 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.
        Area is calculated as size^2.
        """
        return self.__size ** 2
