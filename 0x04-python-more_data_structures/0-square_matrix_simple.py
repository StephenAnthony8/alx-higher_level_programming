#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    n_list = []
    for i in matrix:
        n_i_list = []
        for j in i:
            n_i_list.append(j ** 2)
        n_list.append(n_i_list)
    return (n_list)


if __name__ == "__main__":
    square_matrix_simple()
