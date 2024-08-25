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
            