#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    if idx >= len(my_list) or idx < 0:
        return my_list
    for i in range(0, len(my_list)):
        if i == idx:
            del my_list[i]
        else:
            continue
    return my_list
