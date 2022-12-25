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

    @property
    def size(self):
        """gets the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, square):
        """Implements equals"""
        return self.area() == square.area()

    def __ne__(self, square):
        """Implements not equal"""
        return self.area() != square.area()

    def __gt__(self, square):
        """Implements greater than"""
        return self.area() > square.area()

    def __ge__(self, square):
        """Implements greater or equal to"""
        return self.area() >= square.area()

    def __lt__(self, square):
        """Implements less than"""
        return self.area() < square.area()

    def __le__(self, square):
        """Implements less than or equal to"""
        return self.area() <= square.area()
