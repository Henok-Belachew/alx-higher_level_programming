#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':
    summ = 0
    for i in range(1, len(argv)):
        summ = summ + int(argv[i])
    print("{}".format(summ))
