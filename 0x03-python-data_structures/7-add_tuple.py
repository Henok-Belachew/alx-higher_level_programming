#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    lenA = len(tuple_a)
    lenB = len(tuple_b)
    if lenA == 0:
        tuple_a = (0, 0)
    elif lenA == 1:
        tuple_a = (tuple_a[0], 0)
    if lenB == 0:
        tuple_b = (0, 0)
    elif lenB == 1:
        tuple_b = (tuple_b[0], 0)

    tuple_A = list(tuple_a[:2])
    tuple_B = list(tuple_b[:2])

    for i in range(0, 2):

        a = tuple_A[i]
        b = tuple_B[i]
        result.append(a + b)

    # Returning the result as tuple
    return tuple(result)
