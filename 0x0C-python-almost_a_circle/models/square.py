#!/usr/bin/python3
"""
This module defines class Square, which inherits from class Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        "Initializes attributes from Rectangle class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square.
        Format: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updates the Square by assigning values to attributes."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for index, value in enumerate(args):
                if index < len(attributes):
                    setattr(self, attributes[index], value)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
