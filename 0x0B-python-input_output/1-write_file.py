#!/usr/bin/python3
"""
This module writes to a file and creates the file if it does not exist.
"""


def write_file(filename="", text=""):
    """
    Overwrites a file if it exists.
    Creates the file if it does not exist.
    Returns the numbers of characters written into the file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
