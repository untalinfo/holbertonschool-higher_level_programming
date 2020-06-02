#!/usr/bin/python3
"""
Module of lookup
"""


def lookup(obj):
    """function that returns the list of available
    attributes and methods of an object

    Returns:
        list -- of available attributes and methods
    """
    return dir(obj)
