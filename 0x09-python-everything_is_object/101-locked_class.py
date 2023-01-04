#!/usr/bin/python3
"""comntains a locked class
"""


class LockedClass:
    """ a class with no class or object attributes
    __slots__ defines the only allowed attributes to be created
    dynamically"""

    __slots__ = ['first_name']

    def __init__(self, name=None):
        self.first_name = name
