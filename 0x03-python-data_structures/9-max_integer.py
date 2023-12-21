#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list != []:
        val = int(my_list[0])
    else:
        return ("None")

    for i in range(0, len(my_list)):
        cur_val = int(my_list[i])
        if val < cur_val:
            val = cur_val
    return (val)


if __name__ == "__main__":
    max_integer()
