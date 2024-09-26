# Problem URL:https://leetcode.com/problems/delete-node-in-a-bst/
# TODO: Implement the solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # for find minimum value in BST
    def minNode(self,root):
        current=root
        while current and current.left:
            current=current.left
        return current
    # for find maximum value in BST
    def maxNode(self,root):
        current=root
        while current and current.right:
            current=current.right
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            tempNode=self.minNode(root.right)
            root.val=tempNode.val
            root.right=self.deleteNode(root.right,tempNode.val)
        return root

    