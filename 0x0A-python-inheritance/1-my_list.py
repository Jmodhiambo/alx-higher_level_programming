#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.

The class includes a public method to print the list in ascending order.
"""


class MyList(list):
    """
    A subclass of list that provides a method to print a sorted version
    of the list (ascending order).
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method does not modify the original list; it simply prints
        a sorted copy of the list.
        """
        print(sorted(self))
