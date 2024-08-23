# Problem: Left_View_of_Binary_Tree
# URL: https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

#User function Template for python3
from collections import deque

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    if not root: return []
    res=[]
    q=deque([root])
    while q:
        for i in range(len(q)):
            curr=q.popleft()
            if i==0:
                res.append(curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return res
