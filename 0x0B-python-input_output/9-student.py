#!/usr/bin/python3
"""
This module defines a Student class with public attributes and a method
to retrieve a dictionary representation for JSON serialization.
"""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        with simple data structures
            - list, dictionary, string, integer, and boolean.
        """
        return self.__dict__
