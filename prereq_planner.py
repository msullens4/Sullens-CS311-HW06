"""
Homework 6: The Prerequisite Planner -- starter.

Complete has_cycle and topological_sort below. See
Homework 6 The Prerequisite Planner.md, Part B, for the full requirements.
"""

from typing import Dict, List, Optional


def has_cycle(graph: Dict[str, List[str]]) -> bool:
    """
    Recursive DFS. Track both a permanent "visited" set and a
    temporary "on the current recursion path" set to detect back
    edges (Part A, Question 4). Must work across disconnected
    components.
    """
    # TODO
    visited = set()
    on_path = set()

    def dfs(vertex: str) -> bool:
        if vertex in visited:
            return False

        if vertex in on_path:
            return True

        on_path.add(vertex)

        for neighbor in graph.get(vertex, []):
            if dfs(neighbor):
                return True

        on_path.remove(vertex)
        visited.add(vertex)

        return False
    for vertex in graph:
        if dfs(vertex):
            return True
    return False


def topological_sort(graph: Dict[str, List[str]]) -> Optional[List[str]]:
    """
    Return a valid topological order via DFS finish-time ordering
    (Part A, Questions 2-3), or None if the graph contains a cycle.
    """
    # TODO
    if has_cycle(graph):
        return None

    visited = set()
    finish_order = []

    def dfs(vertex: str) -> None:
        if vertex in visited:
            return 

        visited.add(vertex)

        for neighbor in graph.get(vertex, []):
            dfs(neighbor)

        finish_order.append(vertex)

    for vertex in graph:
        dfs(vertex)

    finish_order.reverse()

    return finish_order


