#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for m in range(0, len(matrix)):
        for n in range(0, len(matrix[m])):
            sepa = "\n" if n + 1 == len(matrix[m]) else " "
            print("{:d}".format(matrix[m][n]), end=sepa)
