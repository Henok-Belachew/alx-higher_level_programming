#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end= "")
        print()
    except IndexError:
        print("Number of list provided out range")
