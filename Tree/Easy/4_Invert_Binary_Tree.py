# Problem: Invert_Binary_Tree
# URL: https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        new_root=TreeNode(root.val)
        if root.left:
            new_root.right=self.invertTree(root.left)
        if root.right:
            new_root.left=self.invertTree(root.right)

        return new_root