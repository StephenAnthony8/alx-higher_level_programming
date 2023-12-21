#!/usr/bin/python3
"""
    Module 0-add_integer - contains function add integer
"""


def add_integer(a, b=98):
    """
        add_integer - adds a to b
        @a: int
        @b: int
        Return: sum value
    """
    val = None
    if type(a) in (int, float):
        if type(b) in (int, float):
            return (int(a) + int(b))
        else:
            val = 'b'
    else:
        val = 'a'
    if val is not None:
        raise TypeError("{} {}".format(val, "must be an integer"))
    return
