#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{}".format(i))
    else:
        if i < 10:
            print("0{}, ".format(i), end="")
        else:
            print("{}, ".format(i), end="")
