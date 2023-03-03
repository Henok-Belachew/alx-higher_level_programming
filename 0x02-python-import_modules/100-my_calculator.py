#!/usr/bin/python3

# Importing necessary functions and modules

from calculator_1 import add, sub, mul, div
from sys import argv

# Possible operations

operators = ["+", "-", "*", "/"]

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])

        if argv[2] == "+":
            print("{:d} {} {:d} = {:d}".format(a, argv[2], b, add(a, b)))
        elif argv[2] == "-":
            print("{:d} {} {:d} = {:d}".format(a, argv[2], b, sub(a, b)))
        elif argv[2] == "*":
            print("{:d} {} {:d} = {:d}".format(a, argv[2], b, mul(a, b)))
        elif argv[2] == "/":
            print("{:d} {} {:d} = {:d}".format(a, argv[2], b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            quit(1)
