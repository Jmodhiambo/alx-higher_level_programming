#!/usr/bin/python3
"""
   Module 4-rectangle
   Defines class rectangle by:
       - Private instance attribute width and height
"""


class Rectangle:
    """Defines a rectangle based on private instance width and height"""
    def __init__(self, width=0, height=0):
        """Instantiates width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area."""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints rectangle with character #."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rect_list = []
            for i in range(self.__height):
                rect_list.append("#" * self.__width)

        return "\n".join(rect_list)

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return (f"Rectangle({self.__width}, {self.__height})") 
