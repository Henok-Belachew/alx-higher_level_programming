#!/usr/bin/python3

def print_last_digit(number):
    if number > 0:
        lastDigit = number % 10
    elif number < 0:
        lastDigit = ((-number) % 10)
    else:
        lastDigit = 0
    print(lastDigit, end="")
    return(lastDigit)
