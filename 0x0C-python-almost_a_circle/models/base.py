#!/usr/bin/python3

"""This module defines a base class"""
import json


class Base:
    """Defines a base object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for base object

        Attribute:
            id(int): the id of instance objects
        """
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string converter"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the objects to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as theFile:
            if not list_objs:
                theFile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                theFile.write(Base.to_json_string(list_dicts))
