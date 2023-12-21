#!/usr/bin/python3
# safe_print_list - print a list via indexing safely
# my_list: list to be accessed
# x: index iterator
# Return: Number of values printed
def safe_print_list(my_list=[], x=0):
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError as e:
            print("")
            return (i)
    print("")
    return (x)
