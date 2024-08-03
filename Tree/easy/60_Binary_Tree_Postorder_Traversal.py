# Problem: Binary_Tree_Postorder_Traversal
# URL: https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return
        # def postOrder(root,ele):
        #     if root.left:
        #         postOrder(root.left,ele) 
        #     if root.right:
        #         postOrder(root.right,ele)
        #     ele.append(root.val)
        # ele=[]
        # postOrder(root,ele)
        # return ele
        
        ## iterative approach
        if not root:
            return
        stack1=[]
        stack2=[]
        current=root
        stack1.append(current)
        while stack1:
            current=stack1.pop()
            stack2.append(current.val) 
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        traversed=[]
        while stack2:
            data=stack2.pop()
            traversed.append(data)
        return traversed
