# Problem: Binary_Tree_Representation
# URL: https://www.geeksforgeeks.org/problems/binary-tree-representation/1

class Solution:
    def createTree(self, root, l):
        # Code here
        q=[root]
        index=1
        while index<len(l):
            curr_node=q.pop(0)
            
            if index<len(l):
                curr_node.left=Node(l[index])
                q.append(curr_node.left)
                index+=1
                
            if index<len(l):
                curr_node.right=Node(l[index])
                q.append(curr_node.right)
                index+=1
                
        return root