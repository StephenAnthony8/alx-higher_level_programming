#!/usr/bin/python3
""" 1-Square - Module containing Square class"""


class Square:
    """ Class Square - Creates a class of square"""

    def __init__(self, size=0):
        """ parameter __size - private instance of the class module"""

        self.__size = size
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """ size - returns the size property
        - currently acts like the creator of the size property as well
        ...
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ size setter - sets the size if both conditions are met"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ area - method of the Square class"""

        return (self.__size * self.__size)

    def my_print(self):
        """ my_print - prints out the square in '#' format"""

        side = self.__size
        if type(side) is not int:
            raise TypeError("size must be an integer")
        elif side < 0:
            raise ValueError("size must be >= 0")

        if (side <= 0):
            print("")
        for i in range(0, side):
            for j in range(0, side):
                print("{}".format("#"), end="")
            print("")
