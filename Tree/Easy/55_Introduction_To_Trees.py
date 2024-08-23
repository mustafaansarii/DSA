# Problem: Introduction_To_Trees
# URL: https://www.geeksforgeeks.org/problems/introduction-to-trees/1

class Solution:
    def countNodes(self, i):
        # Code here
        if i==1: return 1;
        return 2*self.countNodes(i-1);