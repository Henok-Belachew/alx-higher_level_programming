#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    newList = []
    if idx >= len(my_list) or idx < 0:
        return my_list
    for i in range(0, len(my_list)):
        if i == idx:
            continue
        else:
            newList.append(my_list[i])
    return newList
