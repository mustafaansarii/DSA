# Problem URL: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# TODO: Implement the solution

class Node:
    def __init__(self,val) -> None:
        self.left=None
        self.right=None
        self.val=val

    def insert(self,root,data):
        if not root: return Node(data)
        if root.val==data: return root
        if root.val>data: root.left=self.insert(root.left,data)
        elif root.val<data: root.right=self.insert(root.right,data)
        return root

    def searchNode(self,root,key):
        if root:
            if root.val==key: return True
            if root.val>key: return self.searchNode(root.left,key)
            else: return self.searchNode(root.right,key)
        return -1
        

    def LevelOrder(self,root):
        if not root:
            return
        result=[]
        Queue=[root]
        while Queue:
            curr=Queue.pop(0)
            result.append(curr.val)
            if curr.left:
                Queue.append(curr.left)
            if curr.right:
                Queue.append(curr.right)
        return result
    
if __name__ == "__main__":
    root = Node(40)
    root.insert(root, 23)
    root.insert(root, 43)
    root.insert(root, 33)
    root.insert(root, 53)
    root.insert(root, 63)
    
    print("Level Order Traversal:", root.LevelOrder(root))
    print("Search for 23:", root.searchNode(root, 23))
    print("Search for 100:", root.searchNode(root, 100))