#!/usr/bin/python3
"""
    2-append_write - function containing function 'append_write'
"""


def append_write(filename="", text=""):
    """
        append_write - creates or adds into a file with 'text' content
        @filename: file to be created / added onto
        @text: content to write into 'filename'
    """
    rtn_len = 0
    with open(filename, 'a') as file:
        rtn_len = file.write(text)
        # returns number of characters written
    return (rtn_len)
