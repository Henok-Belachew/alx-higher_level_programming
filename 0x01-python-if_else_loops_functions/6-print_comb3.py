#!/usr/bin/python3

for x in range(0, 9):
    y = x
    while y <= 8:
        if x == 8:
            print("{}".format(89))
            break
        else:
            print("{}{}".format(x, y+1), end=", ")
            y = y + 1
