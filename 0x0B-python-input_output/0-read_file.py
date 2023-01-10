#!/usr/bin/python3
'''contains a function
that reads a text file
'''


def read_file(filename=""):
    ''' reads a text file (UTF8)
    and prints it to stdout
    '''
    with open(filename, encoding='utf-8') as afile:
        print(afile.read(), end="")
