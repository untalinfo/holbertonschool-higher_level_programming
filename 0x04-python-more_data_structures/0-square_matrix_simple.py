#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for i in matrix:
        n_matrix.append([j**2 for j in i])
    return n_matrix
