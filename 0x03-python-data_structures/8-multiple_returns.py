#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = (len(sentence))
    first = (sentence[0])
    if lenght == 0:
        return (lenght, None)
    else:
        return (lenght, first)
