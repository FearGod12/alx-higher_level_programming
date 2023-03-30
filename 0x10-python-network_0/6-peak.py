#!/usr/bin/python3
''' contains a fuinction that finds peak '''


def find_peak(list_of_integers):
    '''finds a peak in a list of unsorted integers
    '''
    i = 1
    while i < len(list_of_integers):
        if list_of_integers[i] > list_of_integers[i - 1] and\
                list_of_integers[i] > list_of_integers[i + 1]:
            return list_of_integers[i]
        elif list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return max(list_of_integers)
