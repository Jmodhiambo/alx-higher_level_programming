#!/usr/bin/python3
"""
This modules appends a string to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
