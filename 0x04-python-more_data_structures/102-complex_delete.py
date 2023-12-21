#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    check = 0
    for key in a_dictionary:
        if value == a_dictionary[key]:
            del a_dictionary[key]
            check = 1
            break
    if check == 1:
        complex_delete(a_dictionary, value)
    return (a_dictionary)


if __name__ == "__main__":
    complex_delete()
