#!/usr/bin/python3
""" contains Class Rectabgle with
instance attribut : width and height
property setters :def width(self, value), def height(self, value)
property getters : def width(self), def height(self)
"""


class Rectangle:
    """Rectangle class with instance methods
    getters- width() and height()
    setters - height(value) and width(value)
    where values must be an integer greater than 0
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.heigth = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
