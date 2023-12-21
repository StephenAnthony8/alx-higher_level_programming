#!/usr/bin/python3
"""
    square:
    - Module containing class 'Square'
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square:
        - Class object creating a polygon of Square proportions
        - Inherits from Rectangle as Parent
        - Base is ancestor
    """
    # question 10
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    # question 11
    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.height = self.width = Rectangle.check_function(value, "width")

    # also question 10
    def __str__(self):
        """
            str:
            - public method
            - overriding method
            - returns the object name and its dimensions
        """
        return ("[{}] ({}) {}/{} - {}".format(
            Square.__name__, self.id, self.x, self.y, self.width,))

    # question 12
    def update(self, *args, **kwargs):
        """
            update:
            - public method
            - Assigns arguments to the instance attributes
            @args: dynamic arguments
        """

        if args:
            try:
                super().__init__(
                        self.width, self.height, self.x, self.y, id=args[0])

                self.height = self.width = Rectangle.check_function(
                        args[1], "width")
                self.x = Rectangle.check_function(args[2], "x")
                self.y = Rectangle.check_function(args[3], "y")
            except IndexError:
                return

        elif kwargs:
            for key in kwargs:
                if (key == 'id'):
                    super().__init__(
                            self.width, self.height,
                            self.x, self.y, id=kwargs[key])
                elif (key == 'size'):
                    self.width = self.height = Rectangle.check_function(
                            kwargs[key], key)
                elif (key == 'x'):
                    self.x = Rectangle.check_function(kwargs[key], key)
                elif (key == 'y'):
                    self.y = Rectangle.check_function(kwargs[key], key)

        else:
            return

    # question 14
    def to_dictionary(self):
        """
            to_dictionary:
            - Public method
            - creates a dictionary containing the given attributes

            Return: dictionary containing id, width, height, x, y
        """
        dict_attr = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'size': self.width
                }
        return (dict_attr)
