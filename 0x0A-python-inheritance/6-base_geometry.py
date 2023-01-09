#!/usr/bin/python3
'''contains a Public instance method: def area(self): that raises an
Exception with the message area() is not implemented'''


class BaseGeometry:
    '''method area() raises an exception'''

    def area(self):
        raise Exception("area() is not implemented")
