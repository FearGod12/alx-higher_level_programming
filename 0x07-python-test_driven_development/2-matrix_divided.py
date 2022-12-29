#!/usr/bin/python3
''' function that divides all elements of a matrix.
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError
    Each row of the matrix must be of the same size,
    otherwise raise a TypeError
    div must be a number (integer or float), otherwise raise a TypeError
    div can’t be equal to 0, otherwise raise a ZeroDivisionError
    All elements of the matrix should be divided by div, rounded
    to 2 decimal places
    Returns a new matrix'''


def matrix_divided(matrix, div):
    '''divides a list of lists matrix
    each element rounded to two decimal places
    returns a new matrix'''
    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matix = []
    lists = []
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if len(matrix) < 2 or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    lenght = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        if len(row) != lenght:
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if not type(col) in [int, float]:
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
            lists.append(round((col / div), 2))
            if col == row[lenght - 1]:
                new_matix.append(lists)
                lists = []
    return new_matix
