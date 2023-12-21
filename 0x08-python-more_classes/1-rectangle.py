#!/usr/bin/python3
"""
   1-rectangle - Module containing Rectangle object
"""


class Rectangle:
    """
       Rectangle - class object with width and object properties
    """
    def __init__(self, width=0, height=0):
        """
            init - initializes the class
            @width: width of Rectangle obj(int)
            @height - height of Rectangle object
        """
        self.__width = self.__height = 0
        list_attr = [width, height]

        c = 0
        for x in list_attr:
            c += 1
            err_str = "width" if c < 2 else "height"
            if (isinstance(x, int) is True):
                if (x < 0):
                    raise ValueError("{} must be >= 0".format(err_str))
            else:
                raise TypeError("{} must be an integer".format(err_str))

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ Returns width attribute """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
            sets the width attribute to value
            @value: value to change width to
        """
        if (isinstance(value, int) is True):
            if (value < 0):
                raise ValueError("{} must be >= 0".format("width"))
        else:
            raise TypeError("{} must be an integer".format("width"))
        self.__width = value

    @property
    def height(self):
        """ Returns height attribute """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
            sets the height attribute to value
            @value: value to change height to
        """
        if (isinstance(value, int) is True):
            if (value < 0):
                raise ValueError("{} must be >= 0".format("height"))
        else:
            raise TypeError("{} must be an integer".format("height"))
        self.__height = value
