#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """ initialization with private attribute size"""

    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area"""

        return self.__size * self.__size
