#!/usr/bin/python3
"""
This module divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix, elements must be
    int or float type

    Arguments:
        matrix {list} -- list of list
        div {[int/float]} -- number of division

    Returns:
        [list] -- [new list]
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list or len(matrix) == 0 or matrix[0] is None:
        raise TypeError(error)

    res = []
    new_matrix = []

    for i in matrix:
        if len(i) == 0:
            raise TypeError(error)

        error2 = "Each row of the matrix must have the same size"
        if len(i) != len(matrix[0]):
                raise TypeError(error2)

        if type(div) != int and type(div) != float:
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")
        for j in i:
            if type(j) != int and type(i) != float:
                raise TypeError(error)
            res.append(round((j / div), 2))
        new_matrix.append(res)
        res = []

    return new_matrix
