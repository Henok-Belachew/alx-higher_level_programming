#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrixn = []
    for i in range(0, len(matrix)-1):
        for j in range(0, len(matrix[i])-1):
            matrixn[i][j] = matrix[i][j] * matrix[i][j] 

