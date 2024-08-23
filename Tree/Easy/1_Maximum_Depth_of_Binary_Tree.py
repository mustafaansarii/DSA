# Problem: Maximum_Depth_of_Binary_Tree
# URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def dfs(root, depth):
            if not root: return depth
            left=dfs(root.left,depth)
            right=dfs(root.right,depth)
            return max(left,right)+1
                       
        return dfs(root, 0)
            