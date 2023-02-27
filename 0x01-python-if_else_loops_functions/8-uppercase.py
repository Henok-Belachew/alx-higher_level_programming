#!/usr/bin/python3

def uppercase(str):
    upper = ""
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            upper = upper + chr(ord(x)-32)
        else:
            upper = upper + x
    print("{}".format(upper))
