#!/usr/bin/python3

def uppercase(str):
    index = 0
    for i in (str):
        if (97 <= ord(i) <= 122):
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("".format(""))
    return
