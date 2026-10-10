
import heapq


def prim_mst(city, start="A"):
    if len(city.nodes()) == 0:
        return [], 0

    if start not in city:
        raise ValueError(f"Unknown starting intersection: {start}")

    visited = {start}
    min_heap = []
    mst_edges = []
    total_cost = 0

    for neighbour, data in city[start].items():
        heapq.heappush(
            min_heap,
            (data["weight"], start, neighbour)
        )

    while min_heap and len(visited) < len(city.nodes()):
        weight, u, v = heapq.heappop(min_heap)

        if v in visited:
            continue

        visited.add(v)
        mst_edges.append((u, v, weight))
        total_cost += weight

        for neighbour, data in city[v].items():
            if neighbour not in visited:
                heapq.heappush(
                    min_heap,
                    (data["weight"], v, neighbour)
                )

    if len(visited) != len(city.nodes()):
        raise ValueError("The road network is disconnected.")

    return mst_edges, total_cost


def kruskal_mst(city):
    parent = {node: node for node in city.nodes()}
    rank = {node: 0 for node in city.nodes()}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return False

        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_b] = root_a
            rank[root_a] += 1

        return True

    edges = sorted(
        (data["weight"], u, v)
        for u, v, data in city.edges(data=True)
    )

    mst_edges = []
    total_cost = 0

    for weight, u, v in edges:
        if union(u, v):
            mst_edges.append((u, v, weight))
            total_cost += weight

            if len(mst_edges) == len(city.nodes()) - 1:
                break

    if len(mst_edges) != max(0, len(city.nodes()) - 1):
        raise ValueError("The road network is disconnected.")

    return mst_edges, total_cost