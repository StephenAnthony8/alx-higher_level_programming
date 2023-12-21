#!/usr/bin/python3
"""
5-save_to_json_file
    '''Functions'''
    - save_to_json__file
"""
import json


def save_to_json_file(my_obj, filename):
    """
        save_to_json_file - saves a JSON representation to a .json file
            * Uses python file IO instead of dumps
        @my_obj: python object to be converted to JSON format
        @filename: file to be saved to
    """
    with open(filename, 'w') as file:
        my_objJSON = json.dumps(my_obj)
        file.write(my_objJSON)
