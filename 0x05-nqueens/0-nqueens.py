#!/usr/bin/python3
""" This module defines a nqueens function. """

import sys


def nqueens(n):
    """
    Computes all the possible positions where n queens can be place
    without being attacked by others, backtracking the feasibility of
    new position based on the previous one.

    Prints a list of the possible positions

    :param n: The number of queens we want to place on the board
    :return: void
    """
    if not n.isdigit():
        print('N must be a number')
        exit(1)
    n = int(n)
    if n < 4:
        print('N must be at least 4')
        exit(1)
    solutions = []

    def backtrack(i, solution_group):
        """
        Backtracks the possible positions where the queens
        can be placed.

        :param i: The first row where the queen is positioned.
        :param solution_group: A list of the possible positions.
        :return: void
        """
        nonlocal solutions

        if i == n:
            solutions.append(solution_group.copy())
            return

        for j in range(n):
            if is_feasible(solution_group, [i, j]):
                solution_group.append([i, j])
                backtrack(i + 1, solution_group)
                solution_group.pop()

    backtrack(0, [])

    for solution in solutions:
        print(solution)


def is_feasible(solution, cur):
    """
    Checks whether the current position is feasible to
    place a queen or not.

    :param solution: The positions of the other queens.
    :param cur: The position to evaluate its feasibility.
    :return: True if it is feasible, False otherwise.
    """
    for row, col in solution:
        if row == cur[0] or col == cur[1]:
            return False
        if abs(cur[0] - row) == abs(cur[1] - col):
            return False

    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: nqueens N')
        exit(1)
    nqueens(sys.argv[1])
