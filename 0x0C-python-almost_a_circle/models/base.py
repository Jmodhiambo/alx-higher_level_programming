#!/usr/bin/python3
"""
This has class Base which is going to be the 'base' of this project.
"""
import json


class Base:
    """This is class Base: the base of this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes id.
        Increments __nb_objects for every initialization that id is None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        Overwrites the file if it is not empty.
        """
        filename = f"{cls.__name__}.json"

        # Convert list_objs to a list of dictionaries (using to_dictionary)
        dlist = [obj.to_dictionary() for obj in list_objs] if list_objs else []

        # Write the JSON string to the file
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dlist))
