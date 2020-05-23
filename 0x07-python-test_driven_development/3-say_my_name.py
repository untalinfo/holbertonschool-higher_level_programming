#!/usr/bin/python3
"""
Module prints the name
"""


def say_my_name(first_name, last_name=""):
    """
    This function print the names

    Arguments:
        first_name {str} -- [firts name]
        last_name {str} -- [empty string] (default: {""})
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
