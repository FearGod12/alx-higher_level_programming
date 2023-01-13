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

    def update(self, *args, **kwargs):
        '''1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the
        instance'''

        if args != ():
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
