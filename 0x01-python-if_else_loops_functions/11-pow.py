#!/usr/bin/python3

def pow(a, b):
    r = 1
    for x in range(0, b if b > 0 else -b):
        r = r * a
    if b < 0:
        return (1 / r)
    else:
        return (r)
