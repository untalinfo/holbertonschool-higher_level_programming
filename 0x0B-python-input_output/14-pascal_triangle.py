#!/usr/bin/python3
"""
Module pascal triangle
"""


def pascal_triangle(n):
    """
    Representing the Pascal’s triangle

    Args:
        n (n): lenght of triangle
    """
    lista = [1, 1]
    new = []
    fin = [[1], [1, 1]]
    if n <= 0:
        return new
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        for i in range(3, n + 1):
            new.append(1)
            for j in range(len(lista) - 1):
                new.append(lista[j] + lista[j + 1])
            new.append(1)
            fin.append(new)
            lista = new.copy()
            new = []
        return(fin)
