#!/usr/bin/python3
''' this module contains a function that indents text'''


def text_indentation(text):
    '''prints a text with 2 new lines after each of these
    characters: ., ? and :
    text must be string '''
    if not type(text) is str:
        raise TypeError("text must be a string")
    new_text = ""
    for i in text:
        if i in [".", "?", ":"]:
            new_text += i
            print(new_text.strip(" ") + "\n")
            new_text = ""
        else:
            new_text += i
    if len(new_text) > 0:
        print(new_text.strip(), end="")
