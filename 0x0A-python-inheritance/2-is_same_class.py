#!/usr/bin/python3
"""
Module is same class
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object
    is exactly an instance of the specified class
    Arguments:
        obj
        a_class

    Returns:
        True or False
    """
    return type(obj) == a_class
