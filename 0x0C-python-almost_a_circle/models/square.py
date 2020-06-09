#!/usr/bin/python3
"""
Module of rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize of a square
        Args:
            size (int): size of square
            x (int, optional): position x. Defaults to 0.
            y (int, optional): position y. Defaults to 0.
            id ([type], optional): Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String magic
        Returns:
            string
        """
        id = str(self.id)
        x = str(self.x)
        y = str(self.y)
        size = str(self.width)
        string = "[Square] (" + id + ") " + x + "/" + y + " - " + size
        return string

    @property
    def size(self):
        """
        Getter
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Assigns an argument
        """
        if args:
            values = ["id", "size", "x", "y"]
            for i, j in zip(args, values):
                setattr(self, j, i)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary representation of a Rectangle
        Returns:
            [dict]: [representation of a rectangle]
        """
        dictionary = {}
        for key, values in self.__dict__.items():  # in var(self).items()
            if key.split("__")[-1] == "width"\
                    or key.split("__")[-1] == "height":
                dictionary["size"] = values
            else:
                dictionary[key.split("__")[-1]] = values
        return dictionary
