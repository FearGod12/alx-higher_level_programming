#!/usr/bin/python3
'''contains a Public instance method: def area(self): that raises an
Exception and Public instance method
def integer_validator(self, name, value): that validates value'''


class BaseGeometry:
    '''method area() raises an exception
    method def integer_validator(self, name, value): validates value'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''class of rectangles inherited from class BaseGeometry'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
