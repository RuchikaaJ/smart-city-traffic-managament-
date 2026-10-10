
from collections import deque


def bfs(city, source):
    if source not in city:
        raise ValueError(f"Unknown source intersection: {source}")

    visited = set()
    queue = deque([source])
    order = []

    while queue:
        current = queue.popleft()

        if current in visited:
            continue

        visited.add(current)
        order.append(current)

        for neighbour in city.neighbors(current):
            if neighbour not in visited:
                queue.append(neighbour)

    return order


def dfs(city, source):
    if source not in city:
        raise ValueError(f"Unknown source intersection: {source}")

    visited = set()
    stack = [source]
    order = []

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        order.append(current)

        # Reverse the neighbors to make traversal order predictable.
        neighbours = sorted(city.neighbors(current), reverse=True)

        for neighbour in neighbours:
            if neighbour not in visited:
                stack.append(neighbour)

    return order