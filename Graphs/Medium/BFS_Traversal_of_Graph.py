# Problem URL: https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
            # code here
            visited=set()
            queue=[0]
            result=[]
            while queue:
                node=queue.pop(0)
                if node not in visited:
                    visited.add(node)
                    result.append(node)
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            return result
            


