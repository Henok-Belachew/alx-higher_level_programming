#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """This class is a squeleton for Square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return(1)
        for y in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self):
        if type(value) is tuple:
            if len(value) == 2:
                if type(value[0]) is int and type(value[1]) is int:
                    if value[0] >= 0 and value[1] >= 0:
                        self.__position = value
                        return
        raise TypeError("position must be a tuple of 2 positive integers")
