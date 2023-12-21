#!/usr/bin/python3
""" 101-locked_class - module containing LockedClass object """


class LockedClass:
    """ LockedClass - empty class object """

    def __init__(self):
        """ initializes the class """
        pass

    def __setattr__(self, name, value):
        """ setattr - inbuilt setting checker of attributes for a class"""
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("{} {} '{}'".format(
                "'LockedClass'",
                "object has no attribute",
                name))
