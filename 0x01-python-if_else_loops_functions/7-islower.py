#!/usr/bin/python3
def islower(c):
    """ function that checks for lowercase character.
    :param c: character to be checked if its lower case
    :return: True if lower, False is not
    """
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
