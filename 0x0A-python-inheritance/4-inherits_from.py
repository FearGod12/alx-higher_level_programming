#!/usr/bin/python3
'''contains a function that checks if the object is an instance of class
that inherited (directly or indirectly) from the specified class'''


def inherits_from(obj, a_class):
    '''checks if obj is an instance of a_class'''
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    return False
