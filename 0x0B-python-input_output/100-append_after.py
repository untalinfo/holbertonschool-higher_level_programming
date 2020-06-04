#!/usr/bin/python3
"""
Module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file

    Args:
        filename (str, optional)
        search_string (str, optional) Defaults to "".
        new_string (str, optional) Defaults to "".
    """
    with open(filename, encoding="UTF8") as f:
        string = ""
        for line in f:
            string += line
            if search_string in line:
                string += new_string
    with open(filename, "w", encoding="UTF8") as f:
        f.write(string)
