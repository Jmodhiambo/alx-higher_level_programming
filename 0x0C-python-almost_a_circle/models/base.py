#!/usr/bin/python3
"""
This has class Base which is going to be the 'base' of this project.
"""


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
