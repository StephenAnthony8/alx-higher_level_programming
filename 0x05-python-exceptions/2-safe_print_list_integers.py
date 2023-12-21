#!/usr/bin/python3

# safe_print_list_integers - prints ints only in list
# my_list: list to print from
# x: index length to print
# Return: number of items printed
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
