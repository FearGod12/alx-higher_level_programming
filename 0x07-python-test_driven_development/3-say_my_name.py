#!/usr/bin/python3
'''function that prints My name is <first name> <last name>
 where <first name> and <last name> will be provided by the user'''


def say_my_name(first_name, last_name=""):
    '''prints name
    first_name and last_name must be strings'''
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
