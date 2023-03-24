#!/usr/bin/python3

"""Square Class child of Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Squaer class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor of square class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        str1 = "[Square] ({}) {}/".format(self.id, self.x)
        str2 = "{} - {}".format(self.y, self.width)
        return (str1 + str2)
