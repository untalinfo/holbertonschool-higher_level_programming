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

    def to_json(self, attrs=None):
        """
        dictionary representation of a Student
        """
        if type(attrs) is not list:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            validation = getattr(self, i, None)
            if validation is not None:
                new_dict[i] = validation
        return new_dict

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student
        """
        for key in json:
            self.__dict__[key] = json[key]
