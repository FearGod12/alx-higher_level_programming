#!/usr/bin/python3
'''contains a function
that writes to a file
'''


def write_file(filename="", text=""):
    '''Write string to a text file and
    return the number of characters written'''
    with open(filename, mode='w', encoding='utf-8') as afile:
        char = afile.write(text)
        return char
