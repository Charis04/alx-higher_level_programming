#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    atarashi_matrix = matrix.copy()

    for x in range(len(matrix)):
        atarashi_matrix = list(map(lambda x: x**2, matrix[x]))

    return (atarashi_matrix)
