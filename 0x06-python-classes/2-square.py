#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """This class is a squeleton for Square
    """
    def __init__(self, size=0):
        try:
            self.__size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
