#!/usr/bin/python3

def weight_average(my_list=[]):
    av = sum_v = sum_w = 0

    for i in my_list:
        mult_v = i[0] * i[1]
        sum_v += mult_v
        sum_w += i[1]
    if sum_v and sum_w:
        av = sum_v / sum_w
    return (av)


if __name__ == "__main__":
    weight_average()
