# https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
from typing import List
from heapq import heappush, heappop


class Solution:
    def dijkstra(self, V: int, adj: List[List[List[int]]], S: int) -> List[int]:
        dist = [float('inf')] * V
        dist[S] = 0
        min_heap = [(0, S)]
        while min_heap:
            current_distance, u = heappop(min_heap)
            for neighbor in adj[u]:
                v = neighbor[0]
                weight = neighbor[1]
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heappush(min_heap, (dist[v], v))
        return dist


if __name__ == '__main__':
    solution = Solution()
    V = 5
    adj = [
        [[1, 9], [2, 6], [3, 5], [4, 3]],  # Neighbors of vertex 0
        [[2, 2], [3, 4]],  # Neighbors of vertex 1
        [],  # Neighbors of vertex 2
        [[4, 2]],  # Neighbors of vertex 3
        [[1, 7]]  # Neighbors of vertex 4
    ]
    S = 0

    distances = solution.dijkstra(V, adj, S)
    print("Shortest distances from source:", distances)
