#!/usr/bin/python3
"""This module contain one function called 
    matrix_divided
"""
def matrix_divided(matrix, div):
    """matrix_divided accepts two args, a matrix and a divisor div.
    It returns int rounded to 2 decimal places
    """
    new_matrix = []
    count = 0
    length = 0
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for new in matrix:
        tmp = []
        if count == 0:
            length = len(new)
            count += 1
        if length != len(new):
            raise TypeError("Each row of the matrix must have the same size")
        for i in new:
            if type(i) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            i = i/div
            i = round(i, 2)
            tmp.append(i)
        new_matrix.append(tmp)
    return new_matrix
