#!/usr/bin/python3

# safe_print_division - divides 2 ints safely
# a: int numerator
# b: int denominator
# Return: rtn value
def safe_print_division(a, b):
    try:
        rtn = a / b
    except (ZeroDivisionError, TypeError):
        rtn = None
    finally:
        print("{} {}".format("Inside result:", rtn))
        return (rtn)
