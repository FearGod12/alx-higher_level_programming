#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    columns = len(matrix[0])
    if columns != 0:
        for i in range(rows):
            for j in range(columns):
                if j == columns - 1:
                    print("{:d}".format(matrix[i][j]))
                else:
                    print("{:d}".format(matrix[i][j]), end=" ")
    else:
        print()
