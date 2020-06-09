#!/usr/bin/python3
"""
Module base
"""
import json
import os
import csv


class Base:
    """
    Class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize class base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON string representation
        Returns:
            JSON string
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        """
        filename = cls.__name__ + ".json"
        data = []
        if list_objs is None or list_objs == []:
            data = []
        else:
            for i in list_objs:
                data.append(i.to_dictionary())
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """
        list of the JSON string representation json_string
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances:
        """
        data = []
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            dictionary = cls.from_json_string(f.readline())
        for i in dictionary:
            data.append(cls.create(**i))
        return data

    @classmethod
    def save_to_file_csv(cls, data):
        """
        Save to CSV string
        """

        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if data is not None:
                data = [i.to_dictionary() for i in data]
                sfields = ['id', 'size', 'x', 'y']
                rfields = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == "Rectangle":
                    writer = csv.DictWriter(f, fieldnames=rfields)
                else:
                    writer = csv.DictWriter(f, fieldnames=sfields)
                writer.writeheader()
                writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes in CSV
        """
        filename = cls.__name__ + ".csv"
        sheader = ["id", "size", "x", "y"]
        rheader = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Rectangle":
            header = rheader
        else:
            header = sheader
        result = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.reader(f, delimiter=',')
                for i, row in enumerate(reader):
                    if i > 0:
                        new = cls(1, 1)
                        for x, y in enumerate(row):
                            if y:
                                setattr(new, header[x], int(y))
                        result.append(new)
        return result
