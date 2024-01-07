#!/usr/bin/python3
"""
peak - finds the peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If the mid element is greater than its right neighbor, potential peak is on the left
            right = mid
        else:
            # If the mid element is less than or equal to its right neighbor, potential peak is on the right
            left = mid + 1

    return list_of_integers[left]
