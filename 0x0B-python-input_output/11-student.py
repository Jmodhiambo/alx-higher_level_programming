#!/usr/bin/python3
"""
This module defines a Student class with methods for
retrieving a dictionary representation of the instance
and updating instance attributes from a dictionary.
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
        - If attrs is a list of strings, retrieves the attributes in the list.
        - Otherwise, retrieves all attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with
        key-value pairs from the provided dictionary `json`.
        """
        for key, value in json.items():
            setattr(self, key, value)
