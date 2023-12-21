#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_a = list(a_dictionary.keys())
    key_a.sort()
    for i in key_a:
        print("{}: {}".format(i, a_dictionary[i]))
    return


if __name__ == "__main__":
    print_sorted_dictionary()
