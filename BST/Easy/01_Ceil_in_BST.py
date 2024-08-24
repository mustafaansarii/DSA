# Problem URL: https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1
# TODO: Implement the solution

class Solution:
    def findCeil(self, root, inp):
        def ceil(root, inp):
            if root is None:
                return None
            if root.key == inp:
                return inp
            if root.key > inp:
                left_ceil = ceil(root.left, inp)
                return root.key if left_ceil is None else min(left_ceil, root.key)
            return ceil(root.right, inp)
        ceilhelp = ceil(root, inp)
        return ceilhelp if ceilhelp is not None else -1
