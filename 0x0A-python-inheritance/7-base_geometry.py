#!/usr/bin/python3
"""
Module for base geometry
"""


class BaseGeometry:
    """
    Class base geometry empty
    """
    def area(self):
        """
        Public instance method: def area(self): that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a integer
        Raises:
            TypeError: [must be an integer]
            ValueError: [must be greater than 0]
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
