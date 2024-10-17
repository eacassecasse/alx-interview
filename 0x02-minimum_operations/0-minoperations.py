#!/usr/bin/python3
""" This module defines minOperations function. """

import math


def minOperations(n):
    """
    Computes the minimum amount of operations needed to
    copy the char H n times.
    """
    if not isinstance(n, int):
        return 0

    numOperations = 0
    copied = 1
    clipboard = 0

    while (copied < n):
        if clipboard == 0:
            clipboard = copied
            copied += clipboard
            numOperations += 2
        elif n - copied > 0 and (n - copied) % copied == 0:
            clipboard = copied
            copied += clipboard
            numOperations += 2
        elif clipboard > 0:
            copied += clipboard
            numOperations += 1

    return numOperations
