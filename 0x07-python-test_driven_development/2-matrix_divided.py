#!/usr/bin/python3
"""
This module contains a function to divide
a whole matrix by a constant
"""


def matrix_divided(matrix, div):
    """This function takes a matrix and divides every element by div"""

    """In this double loop i first check if matrix contains valid lists
    with either float or integers to be able to safely apply len() later"""

    if type(matrix) is not list or matrix == [] or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        for i in row:
            if type(i) not in [float, int]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    """Now check if all rows have the same size"""

    iterated_matrix = iter(matrix)
    init_len = len(next(iterated_matrix))
    if not all(len(j) == init_len for j in iterated_matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(
        map(lambda x: list(map(lambda y: round((y / div), 2), x)), matrix)
    )
