#!/usr/bin/python3
"""
Module 102-square
This module defines a class Square by:
    - Private instance attribute: size
    - Property getter and setter for size,
          ensuring it is a number (float or int)
    - Public methods: area to return the square's area
    - Comparator methods to allow comparison of
          Square instances based on area
"""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """
        Initializes the square with size.
        Ensures size is a number and >= 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size.
        Ensures size is a number (float or integer) and >= 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Defines the == comparison based on square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison based on square area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the < comparison based on square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison based on square area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the > comparison based on square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison based on square area."""
        return self.area() >= other
