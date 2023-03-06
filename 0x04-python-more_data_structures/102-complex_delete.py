#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    newDic = a_dictionary.copy()
    for key, Value in newDic.items():
        if value == Value:
            del a_dictionary[key]
    return a_dictionary
