#!/usr/bin/python3

def no_c(my_string):
    new_string = "".join(my_string.split("c"))
    new_string = "".join(new_string.split("C"))
    return (new_string)


if __name__ == "__main__":
    no_c(my_string)
