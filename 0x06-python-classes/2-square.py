#!/usr/bin/python3
"""This module create a new class Square"""


class Square():
    """A square class."""
    def __init__(self, size):
        """Initialization square."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
