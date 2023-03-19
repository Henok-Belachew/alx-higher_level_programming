#!/usr/bin/python3
""" 0-rectangel : module
"""


class Rectangle:
    """ Sekeleton for Rectangle Class
    """
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
