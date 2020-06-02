#!/usr/bin/python3
"""
Module for Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Generate area of rectangle
        Returns:
            int -- area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Create a string
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
