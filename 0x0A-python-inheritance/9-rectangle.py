#!/usr/bin/python3
'''contains a Rectangle class which
inherits from BaseGeometry class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class of rectangles inherited
    from class BaseGeometry'''

    def __init__(self, width, height):
        '''constructor for
        the class'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' returns the area of rectangle
        width multiplied by height'''
        return self.__width * self.__height

    def __str__(self):
        '''prints rectangle object
        nicely on the screen'''
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
