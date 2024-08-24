# Problem URL: https://www.geeksforgeeks.org/problems/merge-two-bst-s/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
# TODO: Implement the solution

class Solution:
    def merge(self, root1, root2):
        # code here
        merged=(self.InOrder(root1)+self.InOrder(root2))
        return sorted(merged)
        
    def InOrder(self,root):
        if not root: return []
        stack=[]
        res=[]
        curr=root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr=curr.left
            elif stack:
                curr=stack.pop()
                res.append(curr.data)
                curr=c