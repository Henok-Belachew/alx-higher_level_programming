#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    ac = len(argv)
    if ac == 1:
        print("{} arguments.".format(ac-1))
    else:
        print("{} arguments:".format(ac - 1))
        for i in range(1, ac):
            print("{}: {}".format(i, argv[i]))
