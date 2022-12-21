#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """ initialization with private attributes size and position"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(position, tuple) is False or len(position) != 2
                or (not isinstance(position[0], int) or
                    (not isinstance(position[1], int))) or
                (position[0] < 0 or position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    def my_print(self):
        """Prints to stdout the square"""
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            val = self.__position[0]
            if val > 0:
                print(' ' * val, end='')
            for j in range(self.__size):
                print('#', end='')
            print()
