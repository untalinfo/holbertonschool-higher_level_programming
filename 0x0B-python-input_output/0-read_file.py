#!/usr/bin/python3
"""
Module of read a file
"""


def read_file(filename=""):
    """
    function that reads a text file
    Keyword Arguments:
        filename {str} -- text file (default: {""})
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        read_file = f.read()
        print(read_file)
