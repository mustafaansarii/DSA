# https://www.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1

from collections import deque
class Solution:
    def modifyQueue(self, q, k):
        # code here
        arr = []

        for i in range(k):
            arr.append(q.popleft())
        for i in range(k):
            q.appendleft(arr[i])
        return q

