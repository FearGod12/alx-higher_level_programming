#!/usr/bin/python3
'''contains a function adds a new
attribute to an object if it’s possible
'''


def add_attribute(obj, key, value):
    '''Adds a new attribute to an object if possible
        Args:
            obj (object): object
            attr: attribute
            value: value to set
            Raises:
                TypeError: if the attribute can't be added
    '''
    if hasattr(obj, "__dict__"):
        if hasattr(obj, "__slots__"):
            if key in obj.__slots__:
                setattr(obj, key, value)
        elif not hasattr(obj, "__slots__"):
            setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
