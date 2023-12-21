#!/usr/bin/python3
"""
    4-from_json_string - module containing function 'from_json_string'
"""
import json


def from_json_string(my_obj):
    """
        from_json_string - dencodes a string to JSON format
        @my_obj: object to be deserialized
        Return: python representation of JSON object
    """
    my_objJSON = json.loads(my_obj)
    return (my_objJSON)
