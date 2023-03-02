#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    totalArgs = len(argv) - 1
    if totalArgs == 0:
        ending = "arguments."
    elif totalArgs == 1:
        ending = "argument:"
    else:
        ending = "arguments:"
    print("{} {}".format(totalArgs, ending))
