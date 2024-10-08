#!/usr/bin/python3
""" This module definies a canUnlockAll function """

from collections import deque


def canUnlockAll(boxes):
    """ Checks whether all the boxes can be unlocked.
    """
    size = len(boxes)
    visited = set([0])
    not_visited = deque(boxes[0])

    while not_visited:
        idx = not_visited.popleft()
        if idx >= size or idx < 0 or idx in visited:
            continue
        visited.add(idx)
        not_visited.extend(boxes[idx])
    return size == len(visited)
