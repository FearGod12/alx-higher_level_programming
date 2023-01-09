#!/usr/bin/python3
''' contains a function that checks if the object
is exactly an instance of the specified class'''


def is_same_class(obj, a_class):
    '''checks if obl is an instance of a_class'''
    if type(obj) is a_class:
        return True
    return False
