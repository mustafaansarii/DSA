import heapq
def single_source_sorted_path(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)
        if curr_distance > distances[curr_node]:
            continue
        for neighbor, weight in graph[curr_node].items():
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print(single_source_sorted_path(graph, "A"))
