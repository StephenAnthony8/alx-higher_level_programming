#!/usr/bin/python3
"""
    6-base_geometry - Module containing baseGeometry class
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
