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
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "\"[]\""
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file
        list_objs is a list of instances who inherits of Base
        example: list of Rectangle or list of Square instances
    If list_objs is None, save an empty list
    The filename must be: <Class name>.json - example: Rectangle.json'''

        alist = []
        if list_objs is not None:
            for each in list_objs:
                alist.append(each.to_dictionary())
        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as afile:
            afile.write(cls.to_json_string(alist))

    def from_json_string(json_string):
        '''returns the list of the JSON string
        representation json_string'''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
