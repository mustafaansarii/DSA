# Problem URL: https://leetcode.com/problems/recover-binary-search-tree
# TODO: Implement the solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def InOrder(root):
            if not root: return []
            res=[]
            stack=[]
            curr=root
            while curr or stack:
                if curr:
                    stack.append(curr)
                    curr=curr.left
                elif stack:
                    curr=stack.pop()
                    res.append(curr)
                    curr=curr.right
            return res
            
        node=InOrder(root)
        swap1,swap2=None,None
        for i in range(len(node)-1):
            if node[i].val>node[i+1].val:
                swap2=node[i+1]
                if not swap1:
                    swap1=node[i]

        swap1.val,swap2.val=swap2.val,swap1.val
