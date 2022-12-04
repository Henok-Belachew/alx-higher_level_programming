#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    if len(argv) == 1:
        print(0)
    else:
        total = 0
        for i in argv[1:]:
            total += int(i)
        print(total)
