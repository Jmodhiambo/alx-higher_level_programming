#!/usr/bin/python3
"""
magic_class.py

This module defines the MagicClass, which represents a circle with a specified radius.
It provides methods to calculate the area and circumference of the circle.

Classes:
    MagicClass: A class to represent a circle with a specific radius.
"""

import math


class MagicClass:
    """
    A class to represent a circle with a specific radius.

    Attributes:
        __radius (float): The radius of the circle. Defaults to 0.

    Methods:
        __init__(radius=0): Initializes the circle with a radius.
        area(): Calculates and returns the area of the circle.
        circumference(): Calculates and returns the circumference..
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass with a radius.

        Parameters:
            radius (int or float): The radius of the circle. Must be a number.

        Raises:
            TypeError: If the radius is not an integer or float.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
