# Problem: Binary_Tree_Inorder_Traversal
# URL: https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return
        # def inOrder(root,ele):
        #     if root.left:
        #         inOrder(root.left,ele)
        #     ele.append(root.val)
        #     if root.right:
        #         inOrder(root.right,ele)
        
        # ele=[]
        # inOrder(root,ele)
        # return ele;
            
        ## iterative approach
        if not root:
            return
        traversed=[]
        stack=[]
        curr=root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr=curr.left
            elif len(stack)>0:
                curr=stack.pop()
                traversed.append(curr.val)
                curr=curr.right
        return traversed

