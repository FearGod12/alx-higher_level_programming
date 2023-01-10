#!/usr/bin/python3
'''contains a Rectangle class which
inherits from BaseGeometry class'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class of squares inherited from
    class Rectangle'''

    def __init__(self, size):
        '''constructor for
        square object'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' returns the area of square
        size multiplied by size'''
        return self.__size ** 2
