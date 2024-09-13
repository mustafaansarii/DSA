from typing import List
class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n

    def find(self,u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return False  # No cycle detected
        return True  # Cycle detected

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        dsu=DSU(V)
        for u in range(V):
            for v in adj[u]:
                if u<v:
                    if dsu.union(u,v):
                        return True
        return False

if __name__ == '__main__':
    V = 5
    # Adjacency list representation of the graph
    adj = [
        [1],  # Adjacency list for vertex 0
        [0, 2, 4],  # Adjacency list for vertex 1
        [1, 3],  # Adjacency list for vertex 2
        [2, 4],  # Adjacency list for vertex 3
        [1, 3]  # Adjacency list for vertex 4
    ]
    print(Solution().isCycle(V,adj))