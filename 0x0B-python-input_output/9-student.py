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

    def to_json(self):
        '''returns a dictionary representation
        of object'''
        return self.__dict__
