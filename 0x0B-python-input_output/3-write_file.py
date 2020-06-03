#!/usr/bin/python3
"""
Module of write in file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file

    Keyword Arguments:
        filename {str} -- text file (default: {""})
        text {str} -- text to write in filen (default: {""})
    """
    with open(filename, 'w', encoding='UTF8') as f:
        file = f.write(text)
    return file
