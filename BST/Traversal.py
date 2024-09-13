from inspect import stack
from queue import Queue
from random import sample


class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data

def insert(root,data):
    if not root:
        return Node(data)
    if root.val == data:
        return root
    if root.val > data:
        root.left = insert(root.left, data)
    elif root.val < data:
        root.right = insert(root.right, data)
    return root

def PreOrder(root):
    if not root: return
    res=[]
    stack=[root]
    while stack:
        curr=stack.pop()
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res

def InOrder(root):
    if not root: return None
    res=[]
    stack=[]
    curr=root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr=curr.left
        elif stack:
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right
    return res

def PostOrder(root):
    if not root: return None
    res=[]
    stack1=[root]
    stack2=[]
    while stack1:
        curr=stack1.pop()
        stack2.append(curr.val)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    while stack2:
        res.append(stack2.pop())
    return  res

def LevelOrder(root):
    if not root: return  None
    Queue=[root]
    res=[]
    while Queue:
        level=[]
        for _ in range(len(Queue)):
            curr=Queue.pop(0)
            level.append(curr.val)
            if curr.left:
                Queue.append(curr.left)
            if curr.right:
                Queue.append(curr.right)
        res.append(level)
    return  res
if __name__=="__main__":
    root=Node(4)
    insert(root,2)
    insert(root,6)
    insert(root,1)
    insert(root,3)
    insert(root,5)
    insert(root,7)
    print("Prerder Traversal: ")
    print(PreOrder(root))
    print("Inorder Traversal: ")
    print(InOrder(root))
    print("PostOrder Traversal: ")
    print(PostOrder(root))
    print("LevelOrder Traversal: ")
    print(LevelOrder(root))