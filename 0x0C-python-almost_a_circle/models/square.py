#!/usr/bin/python3
"""
class Square: iinherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square: inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ method
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size property
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        __str__ method
        """
        return "[Square] ({}) {}/{} - {}".format(
        self.id, self.x, self.y, self.width)
