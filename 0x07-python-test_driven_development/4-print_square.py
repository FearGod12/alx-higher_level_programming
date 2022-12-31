#!/usr/bin/python3
'''contains a function that prints square'''


def print_square(size):
    '''prints a square with the character #
    size is the size length of the square
    size must be an integer'''
    if not type(size) is int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
