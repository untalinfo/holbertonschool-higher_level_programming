#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for row in matrix:
        n_matrix.append([j**2 for j in row])
    return n_matrix
