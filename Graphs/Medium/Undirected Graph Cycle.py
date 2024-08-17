from typing import List

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = set()
        parent = [-1] * V
        def bfs(s):
            queue = [s]
            visited.add(s)

            while queue:
                u = queue.pop(0)
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        parent[v] = u
                        queue.append(v)
                    elif parent[v] != u:
                        return True
            return False

        for i in range(V):
            if i not in visited:
                if bfs(i):
                    return True
        return False