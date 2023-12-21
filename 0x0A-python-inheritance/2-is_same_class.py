#!/usr/bin/python3
"""
    2-is_same_class - Module containing function is_same_class
"""


def is_same_class(obj, a_class):
    """
        is_same_class - checks if obj is an instance of 'a_class'
        @obj: object being checked
        @a_class: class being referenced against
    """
    val = type(obj)
    if (a_class == val):
        return (True)
    else:
        return (False)
