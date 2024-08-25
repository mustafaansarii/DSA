# Problem URL: https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        res=[]
        visited=set()
        stack=[0]
        while stack:
            node=stack.pop()
            if node not in visited:
                visited.add(node)
                res.append(node)
                for  nodes in reversed(adj[node]):
                    if nodes not in visited:
                        stack.append(nodes)
        return res
    
        def dfsrecurssive(node, visited, res):
            visited.add(node)
            res.append(node)
            for nodes in adj[node]:
                if nodes not in visited:
                    visited.add(nodes)
                    dfsrecurssive(nodes, visited, res)
            return res
            
        res=[]
        visited=set()
        return dfsrecurssive(0, visited, res)
        