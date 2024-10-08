#!/usr/bin/python3
"""
   Module 2-rectangle
   Defines class rectangle by:
       - Private instance attribute width and height
"""


class Rectangle:
    """Defines a rectangle based on private instance width and height"""
    def __init__(self, width=0, height=0):
        """Instantiates width and height"""
        self.width = width
        self.height = height

        def width(self):
            """Gets the width"""
            return self.__width

        def width(self, value):
            """Sets the width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")

            self.__width = value

        def height(self):
            """Gets the height"""
            return self.__width

        def width(self, value):
            """Sets the height"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")

            self.__height = value
