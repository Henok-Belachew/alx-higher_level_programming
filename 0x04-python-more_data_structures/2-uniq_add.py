#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = []
    add = 0
    for i in range(0, len(my_list)):
        if my_list[i] in uniq:
            continue
        else:
            add = add + my_list[i]
            uniq.append(my_list[i])
    return add
