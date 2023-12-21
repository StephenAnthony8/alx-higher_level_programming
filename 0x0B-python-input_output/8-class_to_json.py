#!/usr/bin/python3
"""
    8-class_to_json
    - Contains function 'class_to_json'
"""


def class_to_json(obj):
    """
        class_to_json
        - returns a dictionary description of attributes in obj

        @obj: instance object to be checked
        Return: dictionary
    """
    try:
        dict_attr = vars(obj)

    except TypeError:
        dict_var = {}

    return (dict_attr)
