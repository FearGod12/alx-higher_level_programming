#!/usr/bin/python3
'''contains a class MyList that inherits list
Public instance method: def print_sorted(self)
all the elements of the list will be of type int'''


class MyList(list):
    '''
     a class that inherits list class
     '''

    def print_sorted(self):
        '''prints the list in ascending ordwr'''
        new = self[:]
        new.sort()
        print("{}".format(new))
