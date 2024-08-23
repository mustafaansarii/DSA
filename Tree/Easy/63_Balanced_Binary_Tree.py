# Problem: Balanced_Binary_Tree
# URL: https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root: return True

        def dfs(root):
            left,right=0,0
            if root.left:
                left=dfs(root.left)
            if root.right:
                right=dfs(root.right) 
            if left==-1 or right==-1 or abs(left-right)>1:
                return -1
            return max(left,right)+1

        return dfs(root)!=-1