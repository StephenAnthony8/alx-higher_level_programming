#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    len_l = len(my_list) - 1

    for i in range(len_l, -1, -1):
        print("{:d}".format(my_list[i]))


if __name__ == "__main__":
    print_reversed_list_integer()
