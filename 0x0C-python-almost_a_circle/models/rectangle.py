#!/usr/bin/python3
"""
This module writes class Rectangle that inherits from class Base
"""

from models.base import Base


class Rectangle(Base):
    """
    This class inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialized the method of the class
        """
        self.id = id
        super().__init__(self.id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width."""
        self.__width = value

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height."""
        self.__height = value

    @property
    def x(self):
        """Gets the width."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the width."""
        self.__x = value

    @property
    def y(self):
        """Gets the height."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the height."""
        self.__y = value
