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
        if nb_lines <= 0 or nb_lines >= (len(f.readlines())):
            nb_lines = len(f.readlines())
        f.seek(0)
        for i in range(nb_lines):
            print(f.readline(), end='')
