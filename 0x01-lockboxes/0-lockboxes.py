#!/usr/bin/python3
""" This module definies a canUnlockAll function """


class Graph:
    """ Defines a graph"""
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]

    def add_edge(self, u, v):
        """ Adds an edge or relation between two vertices """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start):
        """ Depth-first Search implementation """
        visited = [False] * self.V
        stack = []

        stack.append(start)
        visited[start] = True

        while stack:
            current = stack.pop()

            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True

        return visited


def canUnlockAll(boxes):
    """Verifies whether boxes can be unlocked

    Args:
        boxes (list): The list containing the boxes to be verified.
    Returns:
        True if all the boxes can be unlocked, False otherwise.
    """
    size = len(boxes)
    graph = Graph(size)

    for i in range(0, size):
        for key in boxes[i]:
            if 0 <= key < size:
                graph.add_edge(i, key)

    visited = graph.dfs(0)

    return size == sum(visited)


def toGraph(boxes):
    """Converts a list of list into a graph.

    Args:
        boxes (list): The list to be converted.
    Returns:
        Agraph containing a all the vertices from the list.
    """
    graph = Graph(len(boxes))
    for i in range(0, len(boxes)):
        for key in boxes[i]:
            if key < len(boxes):
                graph.add_edge(i, key)

    return graph
