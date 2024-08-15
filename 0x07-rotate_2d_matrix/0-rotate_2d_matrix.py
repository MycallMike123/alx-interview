#!/usr/bin/python3

"""
Module to rotate a 2D matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):  # loop through the rows
        # we iterate from i+1 to avoid swapping elements twice
        for j in range(i + 1, n):
            # Swap elements to achieve transposition
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

