#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if len(my_list) > idx and idx >= 0:
        my_list.remove(my_list[idx])
    return (my_list)


if __name__ == "__main__":
    delete_at()
