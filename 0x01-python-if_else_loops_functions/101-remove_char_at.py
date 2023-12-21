#!/usr/bin/python3

def remove_char_at(str, n):
    n_str = []
    index_n = 0
    for i in str:
        if (index_n != n):
            n_str.append(i)
        index_n += 1
    n_str = "".join(n_str)
    return (n_str)
