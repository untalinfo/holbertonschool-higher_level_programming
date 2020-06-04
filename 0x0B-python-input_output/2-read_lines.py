#!/usr/bin/python3
"""
Module of read lines a file
"""


def read_lines(filename="", nb_lines=0):
    """
    Read n lines of a file
    Keyword Arguments:
        filename {str} -- text file (default: {""})
        nb_lines {int} -- number of lines (default: {0})
    """
    with open(filename) as f:
        i = len(list(f))
        if nb_lines >= i or nb_lines <= 0:
            nb_lines = i
        f.seek(0, 0)
        for count in range(nb_lines):
            print(f.readline(), end="")
