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
        super().__init__(id)
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints to the stdout the Rectangle instance with character #."""
        if self.y > 0:
            print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, "#" * self.width)

    def __str__(self):
        """
        Updates the class Rectangle by overriding the __str__ method
        so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>.
        """
        # Shorted them to avoid pycodestyle errrr of more 80 words per line
        xx = self.x
        yy = self.y
        ww = self.width
        hh = self.height
        return f"[Rectangle] ({self.id}) {xx}/{yy} - {ww}/{hh}"

    def update(self, *args, **kwargs):
        """Updates the Rectangle by assigning values to attributes."""
        # If *args is not empty, assign values
        if args:
            # This list contains the order of attributes to be updated
            attributes = ["id", "width", "height", "x", "y"]
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        # If *args is empty, use **kwargs
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):  # Check if the attribute exists
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
