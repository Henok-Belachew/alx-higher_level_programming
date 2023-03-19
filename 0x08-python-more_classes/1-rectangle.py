#!/usr/bin/python3
""" 0-rectangel : module
contains a class defination and more related to rectangles.
Class:
    Rectangle: used to define a Rectangle object.
"""


class Rectangle:
    """ Rectangle: class.
    This module contains a definations of A rectangle objects
    and methods to act upon them.
    Args:
        width (optional: int): The widht to instantiate the rectangle object
                               with if not provided it's defaulted to Zero(0).
        height (optional: int): The height  to instantiate the rectangle object
                                with if not provided it's defaulted to Zero().
    Attributes:
        width (int): widht of the rectangle object.
        height (int): height of the rectangle object.
    """

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @width.setter
    def width(self, value):
        """width: property.
        setter property for the privated instance attribute __width.
        Args:
            value (int): The value to set to the private instance attribute.
                         __widht.
        Reuturn:
            None.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @height.setter
    def height(self, value):
        """width: property.
        setter property for the privated instance attribute __height.
        Args:
            value (int): The value to set to the private instance attribute.
                         __height.
        Reuturn:
            None.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
