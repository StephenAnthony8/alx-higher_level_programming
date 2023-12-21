#!/usr/bin/python3
"""
    4-print_square - module that prints a square
"""


def print_square(size):
    """
        print_square - prints a square of size size
        @size - size of square
    """
    if isinstance(size, int) is False:
        raise TypeError("{}".format("size must be an integer"))
    elif size < 0:
        raise ValueError("{}".format("size must be >= 0"))
    for i in range(0, size):
        for j in range(0, size):
            print("{}".format("#"), end="")
        print("")
