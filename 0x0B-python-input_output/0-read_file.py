#!/usr/bin/python3
"""
This module reads a file and prints in to the stdout.
"""


def read_file(filename=""):
    """Reads and prints to stdout the file contents."""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
