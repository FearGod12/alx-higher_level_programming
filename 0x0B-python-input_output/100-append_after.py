#!/usr/bin/python3
'''contains a function that insert a line of text
after a specified line of text in a file
'''


def append_after(filename="", search_string="", new_string=""):
    ''' inserts a line of text to a file, after
    each line containing a specific string
    '''
    new_lines = []
    with open(filename, encoding='utf-8') as afile:
        lines = afile.readlines()
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)

    with open(filename, mode='w', encoding='utf-8') as afile:
        for line in new_lines:
            afile.write(line)
