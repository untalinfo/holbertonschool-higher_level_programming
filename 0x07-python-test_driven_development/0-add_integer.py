#!/usr/bin/python3
"""
This module add two integers
"""


def add_integer(a, b=98):
    """function that adds 2 integers.

    Arguments:
        a {[type]} -- [firts element]
        b {int} -- [second element] (default: {98})

    Raises:
        TypeError: [a must be integer or float]
        TypeError: [b must be integer or float]

    Returns:
        [int] -- [add of integers]
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
