#!/usr/bin/python3
"""
This module writes a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends `new_string` after every line in the file `filename`
    that contains the `search_string`.
    """
    # Step 1: Read all lines into memory
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()  # Read all lines from the file

    # Step 2: Open the file in write mode to overwrite with the modified lines
    with open(filename, mode="w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)  # Write the current line

            # Check if line contains the search string
            if search_string in line:
                # Append new string after the matched line
                f.write(new_string)
