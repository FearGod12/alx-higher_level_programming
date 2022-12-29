#!/usr/bin/python3
''' contains a function that adds two integers.
    a and b must be integers or floats, otherwise raises a TypeError
    exception with the message "a must be an integer or b must be an integer".
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b '''


def add_integer(a, b=98):
    '''adds two integers
    numbers must be integer or float otherwise raise an exception
    if any is float then cast into integer'''
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    elif not type(b) in [int, float]:
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
