#!/usr/bin/python3
"""
Module add attribute
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object if it’s possible
    """
    if hasattr(obj, name) or not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
