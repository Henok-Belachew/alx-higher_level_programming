#!/usr/bin/python3

"""
This module defines `add_integer`
The function returns the sum of a and b
"""


def add_integer(a, b=98):

    """
    Returns the sum of the two argument passed

    Args:
        a(int or float): an integer or float
        b(int or float): has defulat value of 98

    Returns:
        int: the integer sum of the arguments passed

    Raises:
        TypeError: if a or b is not float or int

    Examples:
        >>> add_integer(5, 9)
        14
        >>> add_integer(5.9, 9.8)
        15
        >>> add_integer(-1, -5)
        -6
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a + b)  
