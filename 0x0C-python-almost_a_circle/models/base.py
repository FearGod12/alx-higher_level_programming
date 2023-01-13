#!/usr/bin/python3
'''contains the implementation of a class -
:Base with its attributes and methods
'''
import json


class Base:
    '''base class of models
    The goal of it is to manage
    id attribute in all your future classes
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''class constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "\"[]\""
        else:
            return json.dumps(list_dictionaries)
