#https://leetcode.com/problems/recover-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
        def inorder(root):
            if not root:return []
            return inorder(root.left) + [root] + inorder(root.right)
        
        nodes=inorder(root)
        swap1,swap2=None,None
        for i in range(len(nodes)-1):
            if nodes[i].val>nodes[i+1].val:
                swap2=nodes[i+1]
                if not swap1:
                    swap1=nodes[i]
                else:
                    break

        swap1.val,swap2.val=swap2.val,swap1.val 