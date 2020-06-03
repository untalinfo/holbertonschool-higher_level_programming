#!/usr/bin/python3
"""
Module of write in file
"""


def append_write(filename="", text=""):
    """
    append string to text file

    Keyword Arguments:
        filename {str} -- text file (default: {""})
        text {str} -- text to write in filen (default: {""})
    """
    with open(filename, 'a', encoding='UTF8') as f:
        file = f.write(text)
    return file
