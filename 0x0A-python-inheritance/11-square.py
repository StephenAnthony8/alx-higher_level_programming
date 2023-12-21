#!/usr/bin/python3
"""
    11-square - Module containing Rectangle, square & BaseGeometry classes
"""


class BaseGeometry:
    """
        BaseGeometry - Geometrical class
    """
    def area(self):
        """
        Public Instance method
            area - raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public Instance method
            integer_validator - validates value as an int bigger than 0
            @name: a string
            @value: variable to be validated
            Return: True on success, Exception on error
        """
        if (type(value) is int):
            if (value <= 0):
                raise ValueError("{} must be greater than 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))

        return (True)


class Rectangle(BaseGeometry):
    """
        Rectangle - New class object inheriting from BaseGeometry
        @BaseGeometry: parent class
    """
    def __init__(self, width, height):
        """
        class initialization
        hidden instance attributes
            width - horizontal dimension of object
            height - vertical dimension of object
        """
        inst_att = {"width": width, "height": height}
        for key in inst_att:
            self.integer_validator(key, inst_att[key])

        self.__width = width
        self.__height = height

    def area(self):
        """ area - calculates the area """

        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
        Square - class object of a square
        @Rectangle: parent object
    """

    def __init__(self, size):
        """
        initialization method
            @size: square parameters
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
            area - calculates the area
        """
        return (self.__size ** 2)

    def __str__(self):
        """
            returns the object name alongside the parameters
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
