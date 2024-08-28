# Problem URL: https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
            # code here
            res=[]
            Q=Queue()
            Q.put(0)
            visited=set()
            while not Q.empty():
                node=Q.get()
                if node not in visited:
                    visited.add(node)
                    res.append(node)
                for neighbour in adj[node]:
                    if neighbour not in visited:
                        Q.put(neighbour)
            return res

def bfsOfGraph( V: int, adj: List[List[int]]) -> List[int]:
    visited = [False] * V
    bfs_traversal = []  # List to store the BFS traversal order

    # Loop over all nodes to ensure we cover disconnected components
    for i in range(V):
        if not visited[i]:
            q = Queue()
            q.put(i)
            visited[i] = True

            while not q.empty():
                node = q.get()
                bfs_traversal.append(node)

                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        q.put(neighbor)
                        visited[neighbor] = True

    return bfs_traversal
V = 5
# adj = [
#     [1, 2],  # Adjacency list for node 0
#     [0],     # Adjacency list for node 1
#     [0, 3, 4], # Adjacency list for node 2
#     [2],     # Adjacency list for node 3
#     [2]      # Adjacency list for node 4
#
# ]

adj = [
    [1, 2],  # Adjacency list for node 0
    [0],     # Adjacency list for node 1
    [0],     # Adjacency list for node 2
    [4],     # Adjacency list for node 3
    [3]      # Adjacency list for node 4
]

print(bfsOfGraph(V,adj))

