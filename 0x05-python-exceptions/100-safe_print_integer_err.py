#!/usr/bin/python3
from sys import stderr


# safe_print_integer_err - validates and prints integers
# value: variable to be verified
# Return: True or False depending on validation
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as e:
        stderr.write("{} {}\n".format("Exception:", str(e)))
        return (False)

    return (True)
