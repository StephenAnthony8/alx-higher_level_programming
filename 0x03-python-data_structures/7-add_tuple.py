#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    l_a = list(tuple_a)
    l_b = list(tuple_b)
    l_c = []
    for i in range(0, 2):
        a = 0 if (len(l_a) - 1) < i else l_a[i]
        b = 0 if (len(l_b) - 1) < i else l_b[i]
        l_c.append(int(a) + int(b))

    return (tuple(l_c))


if __name__ == "__main__":
    add_tuple(tuple_a=(), tuple_b=())
