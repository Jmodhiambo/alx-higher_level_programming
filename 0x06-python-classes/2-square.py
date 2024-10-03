#!/usr/bin/python3
"""
Module 2-square
This module defines a class Square by:
    - Private instance attribute: size
    - Instantiation with optional size and validation
"""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """
        Initializes the square.
        Ensures size is an integer and >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
