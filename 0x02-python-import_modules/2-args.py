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

    # Displaying the number of arguments passed
    print("{} {}".format(totalArgs, ending))

    # Printing all the arguments

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
