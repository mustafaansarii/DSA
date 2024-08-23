# Problem: Right_View_of_Binary_Tree
# URL: https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        if not root: return []
        q=[root]
        res=[]
        while q:
            for i in range(len(q)):
                curr=q.pop(0)
                if i==0:
                    res.append(curr.data)
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
        return res

