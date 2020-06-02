#!/usr/bin/python3
"""
Module for Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class square
    """
    def __init__(self, size):
        """Initialize

        Arguments:
            size {int} -- size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area of square
        Returns:
            int -- area
        """
        return self.__size ** 2
