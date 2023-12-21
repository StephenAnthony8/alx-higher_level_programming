#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    ar_1 = len(matrix)
    for i in range(0, ar_1):
        ar_2 = len(matrix[i])
        for j in range(0, ar_2):
            print("{:d}".format(matrix[i][j]),
                  end=" " if j != ar_2 - 1 else "")
        print("{}".format(""))


if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])
