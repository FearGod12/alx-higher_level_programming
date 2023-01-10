#!/usr/bin/python3
'''contains a class MyInt
'''


class MyInt(int):
    '''rebel class from int class
    == and != produces reversed result'''

    def __eq__(self, n2):
        '''returns the opposite of __eq__'''
        return not super().__eq__(n2)

    def __ne___(self, n2):
        '''returns the opposite of __ne__'''
        return not super().__ne__(n2)
