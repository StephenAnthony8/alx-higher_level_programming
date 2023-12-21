#!/usr/bin/python3
""" 1-Square - Module containing Square class"""


class Square:
    """ Class Square - Creates a class of square"""

    def __init__(self, size=0, position=(0, 0)):
        """ parameter __size - private instance of the class module
            parameter __position - private instance of class module
        """

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        check = 0
        if (type(position) is tuple):
            if len(position) == 2:
                for i in position:
                    if type(i) is int and i >= 0:
                        check = 1
                    else:
                        check = 0
                        break

        if check == 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    @property
    def size(self):
        """ size - returns the size property
        - currently acts like the creator of the size property as well
        ...
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ size setter - sets the size if both conditions are met """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ position - sets and returns the postion property of the square """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ position setter - sets the position property in the Square """

        if (type(value) is tuple):
            if len(value) == 2:
                for i in value:
                    if type(i) is int:
                        check = 1
                    else:
                        check = 0
                        break
        if check == 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ area - method of the Square class"""

        return (self.__size * self.__size)

    def my_print(self):
        """ my_print - prints out the square in '#' format"""

        side = self.__size
        pos = self.__position

        if (side <= 0):
            print("")
        else:
            for i in range(0, pos[1]):
                print("")
            for i in range(0, side):
                for k in range(0, pos[0]):
                    print("{}".format(" "), end="")
                for j in range(0, side):
                    print("{}".format("#"), end="")
                print("")
