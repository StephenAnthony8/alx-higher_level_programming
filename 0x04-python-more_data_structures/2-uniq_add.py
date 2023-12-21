#!/usr/bin/python3

def uniq_add(my_list=[]):
    x = 0
    for i in my_list:
        x += i / my_list.count(i)
    return (int(x))


if __name__ == "__main__":
    uniq_add()
