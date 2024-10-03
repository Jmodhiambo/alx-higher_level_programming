#!/usr/bin/python3
"""
Module 1-square
This module defines class Square based on 0-square.py.
"""


class Square:
    """Instatiates attribute size without type or value verification."""

    def __init__(self, value):
       """Initializes a square with a private size attribute."""
       self.__size = value
