#!/usr/bin/python3
"""
    12-pascal_triangle
    - module containing function 'pascal_triangle'
"""


def pascal_triangle(n):
    """
        pascal_triangle
        - returns a 2D list of integers representing a pascal triangle
    """

    rtn = [[1]] if n > 0 else []
    count = 0
    l_append = [1]
    for i in range(1, n):
        append_list = []
        if len(l_append) == 1:
            l_append = l_append + l_append
        else:
            n_list = [a + b for a, b in zip(l_append[1:], l_append[:-1])]
            append_list.append(l_append[0])
            for i in n_list:
                append_list.append(i)
            append_list.append(l_append[-1])
            l_append = append_list
        rtn.append(l_append)

    return (rtn)
