# Problem: Minimum_Element_In_BST
# URL: https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1

#User function Template for python3

"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
"""

class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        ##Your code here
        if (root.left==None):
            return root.data
        return self.minValue(root.left)
     