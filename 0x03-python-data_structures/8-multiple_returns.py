#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        firstChar = None
        lenChar = None
    else:
        firstChar = sentence[0]
        lenChar = len(sentence)
    return (lenChar, firstChar)
