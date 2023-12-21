#!/usr/bin/python3
"""
    0-read_file - Module containing function read_file
"""


def read_file(filename=""):
    """
        read_file - opens, reads and closes a file
        @filename: file to be opened
    """
    with open(filename, 'r') as file:
        file_text = file.read()
        print(file_text, end="")
