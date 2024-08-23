# Problem: Reverse_Level_Order_Traversal
# URL: https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1

def reverseLevelOrder(root):
    # code here
    if not root: return
    # res=[]
    # Q=[root]
    
    # while Q:
    #     level=[]
    #     for _ in range(len(Q)):
    #         curr=Q.pop(0)
    #         level.append(curr.data)
    #         if curr.left:
    #             Q.append(curr.left)
    #         if curr.right:
    #             Q.append(curr.right)
    #     res=level+res
    # return res
        
        
    stack=[]
    Q=[root]
    while Q:
        curr=Q.pop(0)
        if curr.right:
            Q.append(curr.right)
        if curr.left:
            Q.append(curr.left)
        stack.append(curr.data)
    res=[]
    while stack:
        res.append(stack.pop())
    return res