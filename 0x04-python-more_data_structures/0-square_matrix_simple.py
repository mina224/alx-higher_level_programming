#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = [nbr ** 2 for nbr in row]
        new_matrix.append(new_row)
    return new_matrix
