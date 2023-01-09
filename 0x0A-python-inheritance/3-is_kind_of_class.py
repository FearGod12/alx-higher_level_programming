#!/usr/bin/python3
'''contains a function that checks if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class'''


def is_kind_of_class(obj, a_class):
    '''checks if obj is an instance of a_class'''
    return isinstance(obj, a_class)
