class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def insert(root,data):
    if root is None:
        return Node(data)
    if root.data==data:
        return root
    if root.data<data:
        root.right=insert(root.right,data)
    if root.data>data:
        root.left=insert(root.left,data)
    return  root

def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data, end=' ')
        InOrder(root.right)
def preOrder(root):
    if root:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=' ')

if __name__ == '__main__':
    root=Node(100)
    insert(root,34)
    insert(root,54)
    insert(root,74)
    insert(root,38)
    insert(root,30)
    InOrder(root)
    print()
    preOrder(root)
    print()
    postOrder(root)
