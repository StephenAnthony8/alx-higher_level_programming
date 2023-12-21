#!/usr/bin/python3

def best_score(a_dictionary):
    n_key = None
    val = None
    count = 1
    if a_dictionary is not None:
        for key in a_dictionary:
            if a_dictionary[key] is not None and count == 1:
                val = a_dictionary[key]
                count = 0
            if a_dictionary[key] is not None:
                val = a_dictionary[key] if a_dictionary[key] > val else val
                n_key = key if a_dictionary[key] >= val else n_key
    return (n_key)


if __name__ == "__main__":
    best_score()
