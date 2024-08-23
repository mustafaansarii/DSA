# Problem: Leaf_At_Same_Level
# URL: https://practice.geeksforgeeks.org/problems/leaf-at-same-level/1

#User function Template for python3

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        def dfs(level,node,leaf_level):
            if not node: return True
            if not node.left and not node.right:
                if leaf_level[0]==-1:
                    leaf_level[0]=level
                return level==leaf_level[0]
            return dfs(level + 1, node.left, leaf_level) and dfs(level + 1, node.right, leaf_level)
        
        leaf_level=[-1]
        
        return dfs(0,root,leaf_level)