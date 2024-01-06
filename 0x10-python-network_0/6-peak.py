#!/usr/bin/python3
"""
peak - finds the peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ finds the peak in a list of unsorted integers """
    rtn_val = None
    i_list = list_of_integers
    if isinstance(i_list, list) and (len(i_list) > 0):
        x = i_list  # substitution
        rtn_val = x[0]
        for i in range(len(x) - 1):
            if (i > 0) and (x[i] > x[i - 1]) and (x[i] > x[i + 1]):
                rtn_val = x[i]
                break

    return (rtn_val)
