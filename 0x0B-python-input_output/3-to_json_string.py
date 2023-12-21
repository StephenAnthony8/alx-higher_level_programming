#!/usr/bin/python3
"""
    3-to_json_string - module containing function 'to_json_string'
"""
import json


def to_json_string(my_obj):
    """
        to_json_string - encodes a string to JSON format
        @my_obj: object to be serialized
        Return: JSON representation of string
    """
    my_objJSON = json.dumps(my_obj)
    return (my_objJSON)
