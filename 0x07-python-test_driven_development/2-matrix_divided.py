#!/usr/bin/python3
"""
This module has a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all the elements of a matrix
    Raises TypeError incase other data types if not int and floats
    Matrix must have the same size of rows otherwise, TypeError
    div must be an integer and above 0

    Args:
    matrix: The matrix itself
    div: The divisor

    Returns:
    A new matrix which is quotient of the initial matrix
    """
    res = []
    res1 = []
    res2 = []
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if len(matrix) <= 1 or len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    # Checks if there are other datatype apart from integers and floats
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(message)
    if div is None:
        raise TypeError("div must be a number")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        for j in i:
            j = round(j / div, 2)
            if len(res1) < len1:
                res1.append(j)
            else:
                res2.append(j)

    res.append(res1)
    res.append(res2)

    return res
