#!/usr/bin/python3
"""
    1-write_file - function containing function 'write_file'
"""


def write_file(filename="", text=""):
    """
        write_file - creates or overwrites a file with 'text' content
        @filename: file to be created / overwritten
        @text: content to write into 'filename'
    """
    rtn_len = 0
    with open(filename, 'w') as file:
        rtn_len = file.write(text)
        # returns number of characters written
    return (rtn_len)
