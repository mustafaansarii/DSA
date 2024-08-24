
class BST:
    def __init__(self,data):
        self.left=None
        self.val=data
        self.right=None

def insert(root,data):
    if not root: return BST(data)
    if root.val==data: return root
    if root.val>data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
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
    print(f"preOrder Traversal: {res}")

def InOrder(root):
    if not root: return
    stack=[]
    res=[]
    currunt=root
    while stack or currunt:
        if currunt:
            stack.append(currunt)
            currunt=currunt.left
        elif stack:
            currunt=stack.pop()
            res.append(currunt.val)
            currunt=currunt.right
    print(f"InOrder Traversal: {res}")

def PostOrder(root):
    if not root: return
    stack1=[root]
    stack2=[]
    res=[]
    while stack1:
        curr=stack1.pop()
        stack2.append(curr.val)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    while stack2:
        res.append((stack2.pop()))

    print(f"postOrder Traversal: {res}")


def LevelOrder(root):
    if not root: return
    Q=[root]
    res=[]
    while Q:
        Level=[]
        for _ in range(len(Q)):
            curr=Q.pop(0)
            Level.append(curr.val)
            if curr.left:
                Q.append(curr.left)
            if curr.right:
                Q.append(curr.right)
        res.append(Level)
    print(f"LevelOrder Traversal: {res}")


if __name__ == '__main__':
    root=BST(4)
    insert(root,2)
    insert(root,6)
    insert(root,1)
    insert(root,3)
    insert(root,5)
    insert(root,7)

    PreOrder(root)
    InOrder(root)
    PostOrder(root)
    LevelOrder(root)

