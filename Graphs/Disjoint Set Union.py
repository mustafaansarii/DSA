class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.parent[root_u] > self.parent[root_v]:
                self.parent[root_v] = root_u
            if self.parent[root_v] > self.parent[root_u]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.parent[root_u] += 1


if __name__=="__main__":
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 1)]  
    n = 5  # Number of nodes

    # Create a DSU instance
    dsu = DSU(n)

    # Perform union operations
    for i, j in edges:
        dsu.union(i, j)