#!/usr/bin/python3
""" This module defines a rotate_2d_matrix function. """


def rotate_2d_matrix(matrix):
    """
    Rotates in-place a 2D Matrix by 90 degrees.
    :param matrix: The matrix to rotate.
    :return: void
    """
    if not isinstance(matrix, list):
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: isinstance(x, list), matrix)):
        return
    rows = len(matrix)
    columns = len(matrix[0])
    if not all(map(lambda x: len(x) == columns, matrix)):
        return
    column, row = 0, rows - 1
    for i in range(columns * rows):
        if i % rows == 0:
            matrix.append([])
        if row == -1:
            row = rows - 1
            column += 1
        matrix[-1].append(matrix[row][column])
        if column == columns - 1 and row >= -1:
            matrix.pop(row)
        row -= 1
