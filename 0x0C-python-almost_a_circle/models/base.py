#!/usr/bin/python3

"""This module defines a base class"""


class Base:
    """Defines a base object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for base object

        Attribute:
            id(int): the id of instance objects
        """
        if not id:
            Base.__nb_objects += 0
            self.id = Base.__nb_objects
        else:
            self.id = id
