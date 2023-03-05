#!/usr/bin/python3

def square(x=0):
    return x**2


def square_matrix_simple(matrix=[]):
    squared = []
    for r in range(0, len(matrix)):
        sqr = list(map(square, matrix[r]))
        squared.append(sqr)
    return squared
