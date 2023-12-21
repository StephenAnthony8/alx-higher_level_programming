#!/usr/bin/python3

def print_last_digit(number):
    if (type(number) == int):
        last_d = str(number)[-1]
        print(last_d, end="")
    return (int(last_d))
