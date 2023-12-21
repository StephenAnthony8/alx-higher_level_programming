#!/usr/bin/python3

# safe_print_integer - prints only ints
# value: value to be printed
# Return: True if int else false
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return (False)
    return (True)
