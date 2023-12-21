#!/usr/bin/python3
"""
    3-is_kind_of_class - module containing is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class - returns instance & inheritance status of an obj
        @obj: object instance to be compared
        @a_class: class object to be compared to
        Return: True on success, False on Failure
    """
    return (isinstance(obj, a_class))
