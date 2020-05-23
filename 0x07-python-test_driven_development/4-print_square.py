#!/usr/bin/python3
"""
This module generate a square
"""


def print_square(size):
    """
    Print square sizexsize

    Arguments:
        size {integer} -- [area of square]
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
        if type(size) == float:
            raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
