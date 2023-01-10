#!/usr/bin/python3
'''function that appends a string
at the end of a text file
'''


def append_write(filename="", text=""):
    '''appends to file
    creats the file if it doesnt exit
    return the number of chars written
    '''
    with open(filename, mode='a', encoding='utf-8') as afile:
        chars = afile.write(text)
        return chars
