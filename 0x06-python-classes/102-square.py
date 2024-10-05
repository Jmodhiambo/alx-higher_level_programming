#!/usr/bin/python3
"""
This module defines a `Square` class for representing a square.

The `Square` class allows for the creation of square objects with a size.
It provides methods for computing the area of the square, as well as comparison
operators to compare squares based on their area.

Attributes:
-----------
size : int or float
    The size of the square, which must be a non-negative number.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
    -----------
    size : int or float
        The size of the square's side, must be >= 0.

    Methods:
    --------
    area():
        Returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Parameters:
        -----------
        size : int or float, optional
            The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
        --------
        int or float:
            The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        -----------
        value : int or float
            The size must be a number (int or float) and >= 0.

        Raises:
        -------
        TypeError:
            If the size is not a number (int or float).
        ValueError:
            If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
        --------
        int or float:
            The area of the square (size ** 2).
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares if two squares have the same area.

        Parameters:
        -----------
        other : Square or number
            The other square or number to compare with.

        Returns:
        --------
        bool:
            True if both areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return self.area() == other

    def __ne__(self, other):
        """
        Compares if two squares have different areas.

        Parameters:
        -----------
        other : Square or number
            The other square or number to compare with.

        Returns:
        --------
        bool:
            True if areas are not equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return self.area() != other

    def __lt__(self, other):
        """
        Checks if this square's area is less than another's.

        Parameters:
        -----------
        other : Square or number
            The other square or number to compare with.

        Returns:
        --------
        bool:
            True if this square's area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return self.area() < other

    def __le__(self, other):
        """
        Checks if this square's area is less than or equal to another's.

        Parameters:
        -----------
        other : Square or number
            The other square or number to compare with.

        Returns:
        --------
        bool:
            True if this square's area is less than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return self.area() <= other

    def __gt__(self, other):
        """
        Checks if this square's area is greater than another's.

        Parameters:
        -----------
        other : Square or number
            The other square or number to compare with.

        Returns:
        --------
        bool:
            True if this square's area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return self.area() > other

    def __ge__(self, other):
        """
        Checks if this square's area is greater than or equal to another's.

        Parameters:
        -----------
        other : Square or number
            The other square or number to compare with.

        Returns:
        --------
        bool:
            True if this area is greater than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return self.area() >= other
