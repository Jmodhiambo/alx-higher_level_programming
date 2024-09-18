#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        inner_list = []
        for j in i:
            inner_list.append(j**2)

        new_matrix.append(inner_list)

    return (new_matrix)
