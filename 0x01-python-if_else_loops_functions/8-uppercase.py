#!/usr/bin/python3
def uppercase(str):
    c = 0
    for x in str:
        c = 122 - ord(x)
        print("{}".format(chr(90 - c)), end="")
