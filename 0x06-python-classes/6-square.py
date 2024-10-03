#!/usr/bin/python3
"""
Module 6-square
This module defines a class Square by:
    - Private instance attributes: size and position
    - Property getter and setter for size and position
    - Public methods: area and my_print to print square using '#'
"""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with size and position.
        Ensures size is an integer and >= 0, and position is a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method to retrieve the position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position.
        Ensures position is a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square.
        Area is calculated as size^2.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#'.
        If size is 0, prints an empty line.
        The position is used to shift the square using spaces.
        """
        if self.__size == 0:
            print()
        else:
            # Print leading empty lines based on position[1]
            for _ in range(self.__position[1]):
                print()
            # Print the square with spaces at the beginning of each line
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
