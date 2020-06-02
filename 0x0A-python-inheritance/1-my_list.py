#!/usr/bin/python3
"""
Module generate for MyList
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Print the sorted list
        """
        print(sorted(self))
