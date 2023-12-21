#!/usr/bin/python3

def search_replace(my_list, search, replace):
    n_list = []
    for i in my_list:
        n_list.append(replace if i == search else i)
    return (n_list)


if __name__ == "__main__":
    search_replace()
