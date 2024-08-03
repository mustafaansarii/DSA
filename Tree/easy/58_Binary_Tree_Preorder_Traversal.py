# Problem: Binary_Tree_Preorder_Traversal
# URL: https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ele=[]
        # if root:
        #     stack=[]
        #     stack.append(root)
        #     while len(stack)>0:
        #         popped=stack.pop()
        #         ele.append(popped.val)
        #         if popped.right:
        #             stack.append(popped.right)
        #         if popped.left:
        #             stack.append(popped.left)
        #     return ele

        ## Recurssive approach
        def preOrder(node,ele):
            if node:
                ele.append(node.val)
                preOrder(node.left,ele)
                preOrder(node.right,ele)
        ele=[]
        preOrder(root,ele)
        return ele
            

