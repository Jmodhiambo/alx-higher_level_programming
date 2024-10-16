#!/usr/bin/python3
"""
This module writes a function that inserts a line of text to a file,
 after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Append a new string to the new line in current line has a certain string."""
    with open(filename, mode="a+", encoding="utf-8") as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(search_string) > len(word):
                    continue
                if word[0] != search_string[0]:
                    continue
                i = 1
                str_len = len(search_string) - 1
                while i <= str_len
                    if search_string[i] =! word[i]:
                        continue
                    i += 1
            line.seek(2)
            f.write("\n", new_string)               
                    
