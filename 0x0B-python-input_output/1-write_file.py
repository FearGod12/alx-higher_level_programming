#!/usr/bin/python3
'''contains a function
that writes to a file
'''


def write_file(filename="", text=""):
    char = 0
    with open(filename, mode='w', encoding='utf-8') as afile:
        afile.write(text)
    with open(filename, encoding='utf-8') as afile:
        for line in afile:
            char += len(line)
    return char
