#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []
    for i in range(0, (len(my_list))):
        if (idx >= 0) and (len(my_list) > idx):
            if idx == i:
                new_list.append(element)
                continue
        new_list.append(my_list[i])
    return (new_list)


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
