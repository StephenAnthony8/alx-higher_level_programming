#!/usr/bin/python3
"""
    4-inherits_from - Module containing function 'inherits_from'
"""


def inherits_from(obj, a_class):
    """
        inherits_from - Checks if object instance inherits from 'a_class'
        @obj: object to be checked
        @a_class: class to be referenced against
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
