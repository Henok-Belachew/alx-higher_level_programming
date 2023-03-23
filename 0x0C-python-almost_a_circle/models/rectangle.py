#!/usr/bin/python3


"""This module creates a rectangle
It inherits from the ``Base`` class in base.py
"""


from models.base import Base


class Rectangle(Base):
    """Defines Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of a rectangle"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for Width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for Width"""

        self.__width = value

    @property
    def height(self):
        """Getter for Height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""

        self.__height = value

    @property
    def x(self):
        """Getter for x"""

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""

        self.__x = value

    @property
    def y(self):
        """Getter for y"""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter for Y"""

        self.__y = value
