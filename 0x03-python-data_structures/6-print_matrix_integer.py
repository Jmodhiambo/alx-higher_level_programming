#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for j in range(len(rows)):
            if j < len(rows) - 1:
                print("{:d}".format(rows[j]), end=" ")
            else:
                print("{:d}".format(rows[j]), end="")
        print()
