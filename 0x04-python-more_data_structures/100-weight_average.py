#!/usr/bin/python3

def weight_average(my_list=[]):
    add = 0
    mulAdd = 0
    if my_list == []:
        return 0
    for i in range(0, len(my_list)):
        add = add + my_list[i][1]
        mulAdd = mulAdd + (my_list[i][0] * my_list[i][1])
    return (mulAdd/add)
