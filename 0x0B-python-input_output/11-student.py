#!/usr/bin/python3
"""
Module for class Student
"""


class Student:
    """
    Studen class
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize

        Arguments:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """
        dictionary representation of a Student
        """
        return self.__dict__
