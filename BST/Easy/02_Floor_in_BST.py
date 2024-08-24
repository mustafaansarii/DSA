# Problem URL: https://www.geeksforgeeks.org/problems/floor-in-bst/1
# TODO: Implement the solution

class Solution:
    def floor(self, root, x):
        def ceil(root, inp):
            if root is None:
                return None
            if root.data== inp:
                return inp
            if root.data < inp:
                right_ceil = ceil(root.right, inp)
                return root.data if right_ceil is None else max(right_ceil, root.data)
            return ceil(root.left, inp)
        ceilhelp = ceil(root, x)
        return ceilhelp if ceilhelp is not None else -1