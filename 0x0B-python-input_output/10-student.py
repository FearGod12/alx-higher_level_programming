#!/usr/bin/python3
'''contains class Student
with Public instance attributes: first_name, last_name, age
and Public method: def to_json(self)'''


class Student:
    '''class of students
    with methoads and attributes
    '''

    def __init__(self, first_name, last_name, age):
        '''constructor
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns a dictionary representation
        of object'''
        if type(attrs) is list:
            new = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new[attr] = self.__dict__[attr]
            return new
        return self.__dict__
