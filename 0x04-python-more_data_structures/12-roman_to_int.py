#!/usr/bin/python3
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return 0


def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        sum = 0
        i = 0
        while (i < len(roman_string)):
            s1 = value(roman_string[i])
            if (1 + i < len(roman_string)):
                s2 = value(roman_string[i + 1])
                if s1 >= s2:
                    sum = sum + s1
                    i = i + 1
                else:
                    sum = sum + (s2 - s1)
                    i = i + 2
            else:
                sum = sum + s1
                i = i + 1
        return sum
    return 0
