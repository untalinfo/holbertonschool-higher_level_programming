#!/usr/bin/python3
"""
Module of number lines a file
"""


def number_of_lines(filename=""):
    """
    Number of lines in file

    Keyword Arguments:
        filename {str} --  (default: {""})

    Returns:
        int -- lenght of lines in file
    """
    with open(filename, 'r') as f:
        lenFile = len(f.readlines())
    return lenFile
