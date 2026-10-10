
import heapq


def dijkstra(city, source, destination):
    if source not in city or destination not in city:
        raise ValueError("Source or destination is not in the road network.")

    distances = {node: float("inf") for node in city.nodes()}
    previous = {node: None for node in city.nodes()}

    distances[source] = 0
    priority_queue = [(0, source)]
    updates = []

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)

        # Ignore outdated queue entries
        if current_distance > distances[current]:
            continue

        updates.append(
            f"Processing {current}: distance = {current_distance}"
        )

        # Stop when the destination is reached optimally
        if current == destination:
            break

        for neighbour, details in city[current].items():
            travel_time = details["weight"]
            new_distance = current_distance + travel_time

            if new_distance < distances[neighbour]:
                old_distance = distances[neighbour]
                distances[neighbour] = new_distance
                previous[neighbour] = current

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

                updates.append(
                    f"Updated {neighbour}: {old_distance} -> "
                    f"{new_distance} via {current}"
                )

    if distances[destination] == float("inf"):
        return [], float("inf"), updates

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distances[destination], updates
