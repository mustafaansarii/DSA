# Problem: Delete_Node_In_A_BST
# URL: https://leetcode.com/problems/delete-node-in-a-bst/

class Node:
    def __init__(self,data) -> None:
        self.val=data
        self.left=None
        self.right=None
    

class BST:
    def insert(self,root,key):
        if not root:
            return Node(key)
        if root.val>key:
            root.left=self.insert(root.left,key)
        elif root.val<key:
            root.right=self.insert(root.right,key)
        return root
            
            
    def LevelOrder(self,root):
        if not root:
            return root
        queue=[root]
        while queue:
            current=queue.pop(0)
            print(current.val, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def minNode(self,root):
        current=root
        while current and current.left:
            current=current.left
        return current
    
    def maxNode(self,root):
        current=root
        while current and current.right:
            current=current.right
        return current

    def deleteNode(self,root,key):
        if not root:
            return root
        
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            tempNode=self.minNode(root.right)
            root.val=tempNode.val
            root.right=self.deleteNode(root.right,tempNode.val)
        return root

if __name__=="__main__":
    root=Node(5)
    bst=BST()
    arr=[3,6,2,4,7]
    for i in arr:
        bst.insert(root,i)
    bst.LevelOrder(root)
    print()
    bst.deleteNode(root,3)
    bst.LevelOrder(root)
    print()


    