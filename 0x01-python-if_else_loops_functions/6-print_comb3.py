#!/usr/bin/python3
a = 1
for x in range(0, 9):
    for y in range(a, 10):
        pair = str(x)+str(y)
        if pair == "89":
            print(89)
        else:
            print("{}, ".format(pair), end="")
    a += 1
