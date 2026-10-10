
def bellman_ford(city, source, destination):
    if source not in city or destination not in city:
        raise ValueError("Source or destination is not in the road network.")

    distances = {node: float("inf") for node in city.nodes()}
    previous = {node: None for node in city.nodes()}
    distances[source] = 0

    updates = []

    # Bellman-Ford performs at most |V| - 1 passes.
    nodes = list(city.nodes())

    for pass_number in range(len(nodes) - 1):
        changed = False

        for u, v, data in city.edges(data=True):
            weight = data["weight"]

            # Relax the road from u to v.
            if distances[u] != float("inf"):
                candidate = distances[u] + weight

                if candidate < distances[v]:
                    old = distances[v]
                    distances[v] = candidate
                    previous[v] = u
                    changed = True

                    updates.append(
                        f"Pass {pass_number + 1}: "
                        f"{v} improved from {old} to {candidate} via {u}"
                    )

            # Our NetworkX graph is undirected, so also check v to u.
            if distances[v] != float("inf"):
                candidate = distances[v] + weight

                if candidate < distances[u]:
                    old = distances[u]
                    distances[u] = candidate
                    previous[u] = v
                    changed = True

                    updates.append(
                        f"Pass {pass_number + 1}: "
                        f"{u} improved from {old} to {candidate} via {v}"
                    )

        # Stop early if a complete pass makes no changes.
        if not changed:
            break

    # Detect a negative cycle reachable from the source.
    for u, v, data in city.edges(data=True):
        weight = data["weight"]

        if distances[u] != float("inf") and distances[u] + weight < distances[v]:
            raise ValueError("Negative-weight cycle detected.")

        if distances[v] != float("inf") and distances[v] + weight < distances[u]:
            raise ValueError("Negative-weight cycle detected.")

    if distances[destination] == float("inf"):
        return [], float("inf"), updates

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distances[destination], updates