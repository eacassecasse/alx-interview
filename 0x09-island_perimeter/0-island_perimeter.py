#!/usr/bin/python3
""" This module defines a island_perimeter() function. """


def island_perimeter(grid):
    """
    Computes the perimeter of an island located inside the grid.
    :param grid: A 2D array representing the area of the island
    surrounded by water
    :return: the perimeter of the island
    """
    if not isinstance(grid, list):
        return
    if len(grid) > 100 or len(grid[0]) > 100:
        return

    perimeter = 0
    rows = len(grid)

    for i, row in enumerate(grid):
        cols = len(row)
        for j, cell in enumerate(row):
            if cell == 1:
                if i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0):
                    perimeter += 1
                if i == rows - 1 or (
                        len(grid[i + 1]) > j and grid[i + 1][j] == 0):
                    perimeter += 1
                if j == 0 or row[j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or (cols > j + 1 and row[j + 1] == 0):
                    perimeter += 1

    return perimeter
