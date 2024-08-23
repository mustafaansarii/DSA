# Problem: Height_Of_Binary_Tree
# URL: https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        if not root: return 0

        left=self.height(root.left)

        right=self.height(root.right)
        
        return max(right,left)+1
        