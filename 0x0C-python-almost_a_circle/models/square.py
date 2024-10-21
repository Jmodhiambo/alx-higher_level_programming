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

    def __str__(self):
        """
        Returns a string representation of the Square.
        Format: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
