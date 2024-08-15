# Problem URL: https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
class Solution:
        def depth_first_search(self,node,adj,visited=None):
            if visited is None:
                 visited=set()
            result = []
            visited.add(node)
            result.append(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    result.extend(self.depth_first_search(neighbor,adj,visited))
            return result
        
    

if __name__=="__main__":
    graph={
        "5":["3","7"],
        "3":["2","4"],
        "2":[],
        "4":["7"],
        "8":[],
        "7":["8"]
    }
    result=Solution().depth_first_search("5",graph)
    print(result)