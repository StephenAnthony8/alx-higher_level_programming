#!/usr/bin/python3
"""
peak - finds the peak in a list of unsorted integers
"""


def peak_recur(left, arr, right, mid):
    x = len(arr) - 2
    if ((mid > 0) and mid <= (len(arr) - 2)):
        # mid = mid - 1
        pos = [arr[mid - 1], arr[mid], arr[mid + 1]]
        if ((arr[mid] >= arr[mid - 1]) and (arr[mid] >= arr[mid + 1])):
            if (len(set(pos)) != 1):
                return (arr[mid])
            else:
                x = pos[0]
                if left and right:
                    vals = (peak_recur(1, arr, 0, mid - 1),
                            peak_recur(0, arr, 1, mid + 1))
                    if (None not in vals):
                        y = vals[0] if vals[0] > vals[1] else vals[1]
                        return (x if x > y else y)
                    else:
                        y = (vals[0]) if vals[1] is None else vals[1]

                elif left:
                    y = peak_recur(1, arr, 0, mid - 1)
                elif right:
                    y = (peak_recur(0, arr, 1, mid + 1))
                else:
                    return None
                return (x if ((y is None) or (x > y)) else y)
        else:
            if left and right:
                vals = (peak_recur(1, arr, 0, mid - 1),
                        peak_recur(0, arr, 1, mid + 1))
                if (None not in vals):
                    return (vals[0] if vals[0] > vals[1] else vals[1])
                else:
                    return ((vals[0]) if vals[1] is None else vals[1])

            elif left:
                return (peak_recur(1, arr, 0, mid - 1))
            elif right:
                return (peak_recur(0, arr, 1, mid + 1))
            else:
                return (None)
    return (None)


def find_peak(list_of_integers):
    """ finds the peak in a list of unsorted integers """

    peak_index = None
    if (isinstance(list_of_integers, list) and (len(list_of_integers)) > 0):

        mid = len(list_of_integers) / 2

        if (isinstance(mid, float)):
            mid = int(mid)
        peak_index = peak_recur(1, list_of_integers, 1, mid)
    return (peak_index)
