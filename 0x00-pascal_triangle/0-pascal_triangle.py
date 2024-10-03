#!/usr/bin/python3
"""This module defines a pascal triangle function."""


def pascal_triangle(n):
    """Computes a Pascal Triangle.

    Args:
        n (integer): The amount of rows to compute.
    Returns:
        A matrix containing the computed coeficients or any list otherwise.
    """
    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    return triangle
