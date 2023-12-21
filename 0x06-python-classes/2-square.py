#!/usr/bin/python3
""" 1-Square - Module containing Square class"""


class Square:
    """ Class Square - Creates a class of square"""

    def __init__(self, __size=0):
        """ parameter __size - private instance of the class module"""

        self.__size = __size
        if (type(__size) is not int):
            raise TypeError("size must be an integer")
        if (__size < 0):
            raise ValueError("size must be >= 0")
