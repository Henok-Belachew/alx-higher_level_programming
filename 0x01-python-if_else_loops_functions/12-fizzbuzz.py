#!/usr/bin/python3

def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("{:s}".format("FizzBuzz"), end=" ")
        elif x % 3 == 0:
            print("{:s}".format("Fizz"), end=" ")
        elif x % 5 == 0:
            print("{:s}".format("Buzz"), end=" ")
        else:
            print("{:d}".format(x), end=" ")
