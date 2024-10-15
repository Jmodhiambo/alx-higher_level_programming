#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from int but inverts
the equality and inequality operators.
"""


class MyInt(int):
    """A rebel integer class that inverts == and != operators."""

    def __eq__(self, other):
        """
        Invert the equality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal, False if they are equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Invert the inequality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: False if the values are not equal, True if they are equal.
        """
        return super().__eq__(other)
