#!/usr/bin/python3
""" This module definies a canUnlockAll function """


def canUnlockAll(boxes):
    """ Checks whether all the boxes can be unlocked.
    """
    size = len(boxes)
    visited = set([0])
    not_visited = set(boxes[0]).difference(set([0]))
    while len(not_visited) > 0:
        idx = not_visited.pop()
        if not idx or idx >= size or idx < 0:
            continue
        if idx not in visited:
            not_visited = not_visited.union(boxes[idx])
            visited.add(idx)
    return size == len(visited)
