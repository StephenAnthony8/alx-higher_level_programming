#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
        new_dict.update({key: (a_dictionary[key] * 2)})
    return (new_dict)


if __name__ == "__main__":
    multiply_by_2()
