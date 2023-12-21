#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    bool_l = []

    for i in range(0, len(my_list)):
        val = True if int(my_list[i]) % 2 == 0 else False
        bool_l.append(val)
    return (bool_l)


if __name__ == "__main__":
    divisible_by_2()
