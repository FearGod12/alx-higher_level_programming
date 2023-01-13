#!/usr/bin/python3
'''contains  the implementation of class Rectangle that
inherits from Base'''

from models.base import Base
import os


class Rectangle(Base):
    '''Class Rectangle inherits from Base
    Private instance attributes,with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    Class constructor:
    def __init__(self, width, height, x=0, y=0, id=None)'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''class constructor'''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area"""
        return self.__height * self.__width

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        if self.__y != 0:
            for line in range(self.__y):
                print()
        for row in range(self.__height):
            if self.__x != 0:
                for space in range(self.__x):
                    print(" ", end="")
            print("#" * self.__width)

    def __str__(self):
        return (f"[Rectangle] ({self.id})\
 {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute:
    1st argument should be the id attribute
    2nd argument should be the width attribute
    3rd argument should be the height attribute
    4th argument should be the x attribute
    5th argument should be the y attribute'''
        if args != ():
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }
