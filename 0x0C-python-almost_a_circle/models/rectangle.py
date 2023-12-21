#!/usr/bin/python3
"""
    Rectangle:
    Class object that inherits from Base
    - Answers question 2
"""
from models.base import Base


class Rectangle(Base):
    """
        Rectangle:
        - Creates polygon of Rectangle proportions
        - Inherits from 'Base' object
        - Parent to Square class
    """
    @staticmethod
    def check_function(value, label):
        """
            check_function:
            - static method
            - validates the value according to the parameters of its label

            @value: variable to be validated
            @label: name of variable
        """
        if (type(value) == int):
            if (value == 0 and label in ['x', 'y']):
                return (value)
            elif (value > 0):
                return (value)
            else:
                raise ValueError("{} must be {} 0".format(
                    label, ">=" if label in ["x", 'y'] else '>'))
        else:
            raise TypeError("{} must be an integer".format(label))

    # question 2
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialization of Rectangle instance
        """

        super().__init__(id)
        args_dict = {
                "width": width,
                "height": height,
                "x": x,
                "y": y
                     }

        for key in args_dict:
            if (type(args_dict[key]) != int):
                raise TypeError("{} must be an integer".format(key))

            elif (args_dict[key] <= 0 and key in ["width", "height"]):
                raise ValueError("{} must be > 0".format(key))

            elif (args_dict[key] < 0 and key in ["x", "y"]):
                raise ValueError("{} must be >= 0".format(key))

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # question 3
    @property
    def width(self):
        """
            width:
            - property method
            - returns the private attr instance width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
            width:
            - setter method
            - sets the private attr instance width to 'value'

            @value: value to set private attribute to if int & > 0
        """
        label = "width"
        self.__width = Rectangle.check_function(value, label)

    @property
    def height(self):
        """
            height:
            - property method
            - returns the private attr instance height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
            height:
            - setter method
            - sets the private attr instance height to 'value'

            @value: value to set private attribute to if int & > 0
        """
        label = "height"
        self.__height = Rectangle.check_function(value, label)

    @property
    def x(self):
        """
            x:
            - property method
            - returns the private attr instance x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
            x:
            - setter method
            - sets the private attr instance x to 'value'

            @value: value to set private attribute to if int & > 0
        """
        label = 'x'
        self.__x = Rectangle.check_function(value, label)

    @property
    def y(self):
        """
            y:
            - property method
            - returns the private attr instance y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
            width:
            - setter method
            - sets the private attr instance y to 'value'

            @value: value to set private attribute to if int & > 0
        """
        label = "y"
        self.__y = Rectangle.check_function(value, label)

    # question 4
    def area(self):
        """
            area:
            - public method
            - returns the area value of the Rectangle instance
        """
        return (self.__height * self.__width)

    # question 5 & 7
    def display(self):
        """
            display:
            - public method
            - prints to stdout a rectangle object of '#' characters
        """
        for _ in range(self.__y):
            print("")

        for i in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")

            for j in range(self.__width):
                print("#", end="")

            print("")

    # question 6
    def __str__(self):
        """
            str:
            - public method
            - overriding method
            - returns the object name and its dimensions
        """
        return ("[{}] ({}) {}/{} - {}/{}".format(Rectangle.__name__,
                                                 self.id,
                                                 self.__x,
                                                 self.__y,
                                                 self.__width,
                                                 self.__height
                                                 ))

    # question 8, 9
    def update(self, *args, **kwargs):
        """
            update:
            - public method
            - Assigns arguments to the instance attributes
            @args: dynamic arguments
        """

        if args:
            try:
                super().__init__(id=args[0])
                self.__width = Rectangle.check_function(args[1], "width")
                self.__height = Rectangle.check_function(args[2], "height")
                self.__x = Rectangle.check_function(args[3], "x")
                self.__y = Rectangle.check_function(args[4], "y")
            except IndexError:
                return

        elif kwargs:
            for key in kwargs:
                if (key == 'id'):
                    super().__init__(id=kwargs[key])
                elif (key == 'height'):
                    self.__height = Rectangle.check_function(kwargs[key], key)
                elif (key == 'width'):
                    self.__width = Rectangle.check_function(kwargs[key], key)
                elif (key == 'x'):
                    self.__x = Rectangle.check_function(kwargs[key], key)
                elif (key == 'y'):
                    self.__y = Rectangle.check_function(kwargs[key], key)

        else:
            return

    # question 13
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
                'width': self.width,
                'height': self.height,
                }
        return (dict_attr)
