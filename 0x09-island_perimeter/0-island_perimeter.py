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
    island = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                island.append(grid[i][j])

    if len(island) == 0:
        return 0
    perimeter = 0
    for i in range(len(island)):
        if i == 0 or i == len(island) - 1:
            perimeter += 3 * island[i]
        else:
            perimeter += 2 * island[i]

    return perimeter
