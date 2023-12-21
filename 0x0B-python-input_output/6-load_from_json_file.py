#!/usr/bin/python3
"""
6-load_from_json_file
    '''Functions'''
    - load_from_json__file
"""
import json


def load_from_json_file(filename):
    """
        load_from_json_file
            - reads a JSON file and decodes its content to a python object
            - Uses python file IO instead of load

        @filename: file to be read from
        Return: created python object
    """
    with open(filename, 'r') as file:
        rtn_obj = json.loads(file.read())
    return (rtn_obj)
