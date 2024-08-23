# Problem: Binary_Tree_Level_Order_Traversal
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal/

def Binary_Tree_Level_Order_Traversal(root):
    # TODO: Implement the solution for Binary_Tree_Level_Order_Traversal
    if not root: return 

    Q=[root]
    res=[]

    while Q:
        level=[]
        for _ in range(len(Q)):
            curr=Q.pop(0)
            level.append(curr.val)
            if curr.left:
                Q.append(curr.left)

            if curr.right:
                Q.append(curr.right)
        res.append(level)

    return res


        
