#!/usr/bin/python3
"""
    2-matrix_divided.py - matrix division module
    matrix_divided: function dividing the matrices
"""


def matrix_divided(matrix, div):
    """
        matrix_divided - divides all elements of a matrix
        @matrix: matrix to be divided
        @div: dividing value
        Return: new matrix
    """

    if type(div) not in (int, float):
        raise TypeError("{}".format(
            "div must be a number"
            ))
    elif (div == 0):
        raise ZeroDivisionError("{}".format(
            "division by zero"
            ))
    elif isinstance(matrix, list) is False:
        raise TypeError("{}".format(
            "matrix must be a matrix (list of lists) of integers/floats"
            ))
    main_list = []
    try:
        len_original = len(matrix[0])
    except IndexError as e:
        raise TypeError("{} {}".format(
            "matrix must be a matrix",
            "(list of lists) of integers/floats"
            ))
    for i in matrix:
        len_next = len(i)
        if len_original != len_next:
            raise TypeError("{}".format(
                "Each row of the matrix must have the same size"
                ))
        mini_list = []
        if isinstance(i, list) is False:
            raise TypeError("{}".format(
                "matrix must be a matrix (list of lists) of integers/floats"
                ))
        try:
            inside_list = i[0]
        except IndexError as e:
            raise TypeError("{} {}".format(
                "matrix must be a matrix",
                "(list of lists) of integers/floats"
                ))
        for j in i:

            if type(j) not in (int, float):
                raise TypeError("{} {}".format(
                    "matrix must be a matrix",
                    "(list of lists) of integers/floats"
                    ))
            mini_list.append(float("{:.2f}".format(j / div)))
        main_list.append(mini_list)
    return (main_list)
