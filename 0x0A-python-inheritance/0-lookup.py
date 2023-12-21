#!/usr/bin/python3
"""
    0-lookup - contains function lookup
"""


def lookup(obj):
    """
        lookup - returns all attributes and methods of an object
        obj: object to be checked
        Return: list to be checked
    """
    list_obj = []
    list_obj = dir(obj)
    return (list_obj)
