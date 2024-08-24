# Problem URL: https://www.geeksforgeeks.org/problems/binary-tree-to-bst/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
# TODO: Implement the solution

# User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        values = []
        self.InOrder(root, values)
        values.sort()
        index = [0]

        def array_to_BST(root):
            if root is None: return
            array_to_BST(root.left)
            root.data = values[index[0]]
            index[0] += 1
            array_to_BST(root.right)

        array_to_BST(root)
        return root

    def InOrder(self, root, values):
        if root is None:
            return
        self.InOrder(root.left, values)
        values.append(root.data)
        self.InOrder(root.right, values)