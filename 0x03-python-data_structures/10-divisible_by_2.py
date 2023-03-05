#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    theList = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            theList.append(True)
        else:
            theList.append(False)
    return theList
