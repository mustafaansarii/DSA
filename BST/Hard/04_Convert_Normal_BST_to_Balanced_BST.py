# Problem URL: https://www.geeksforgeeks.org/convert-normal-bst-balanced-bst/
# TODO: Implement the solution

class Solution:
    def buildBalancedTree(self,root):
        #code here
        def InOrder(root):
            if not root: return []
            res=[]
            stack=[]
            curr=root
            while curr or stack:
                if curr:
                    stack.append(curr)
                    curr=curr.left
                elif stack:
                    curr=stack.pop()
                    res.append(curr)
                    curr=curr.right
            return res
            
        def buildBalancedBST(nodes,start,end):
            if start>end: return None
            mid=(start+end)//2
            root=nodes[mid]
            root.left=buildBalancedBST(nodes,start,mid-1)
            root.right=buildBalancedBST(nodes,mid+1,end)
            return root
        
        nodes=InOrder(root)
        return buildBalancedBST(nodes,0,len(nodes)-1)