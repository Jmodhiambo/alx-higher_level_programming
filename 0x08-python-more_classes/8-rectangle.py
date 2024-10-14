#!/usr/bin/python3
"""
   Module 8-rectangle
   Defines class rectangle by:
       - Private instance attribute width and height
"""


class Rectangle:
    """Defines a rectangle based on private instance width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiates width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                rect_list.append(str(self.print_symbol) * self.__width)

        return "\n".join(rect_list)

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Deletes an instance."""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
