#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list == []:
        return None
    else:
        maxNum = my_list[0]
        for i in range(0, len(my_list)):
            if my_list[i] > maxNum:
                maxNum = my_list[i]
        return maxNum
