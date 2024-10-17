#!/usr/bin/python3
"""
This module defines a Student class with a method that retrieves
a dictionary representation of a Student instance.
"""


class Student:
    """Defines a student by first_name, last_name, and age."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        - If attrs is a list of strings, only retrieves the attributes in the list.
        - Otherwise, retrieves all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
