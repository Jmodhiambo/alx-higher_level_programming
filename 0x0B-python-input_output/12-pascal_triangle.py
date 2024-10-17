#!/usr/bin/python3
"""
This module contains a function that generates Pascal's triangle.

The function pascal_triangle(n) returns a list of lists representing
the Pascal's triangle of size n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.

    Args:
        n (int): The number of levels in Pascal's triangle.

    Returns:
        List of lists representing Pascal's triangle,
        or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Generate each row of Pascal's triangle
    for i in range(1, n):
        # Start each row with '1'
        row = [1]
        # Add the middle elements,
        # which are the sum of the two elements directly above
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with '1'
        row.append(1)
        triangle.append(row)

    return triangle
