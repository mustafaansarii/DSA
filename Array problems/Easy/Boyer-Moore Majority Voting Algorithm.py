#https://www.geeksforgeeks.org/problems/majority-element-1587115620/1?page=1&status=unsolved&sortBy=submissions
class Solution:
    def majorityElement(self, arr, n):
        candidate = -1
        votes = 0
        for i in range (n):
            if (votes == 0):
                candidate = arr[i]
                votes = 1
            else:
                if (arr[i] == candidate):
                    votes += 1
                else:
                    votes -= 1
        count = 0
        
        for i in range (n):
            if (arr[i] == candidate):
                count += 1
                
        if (count > n // 2):
            return candidate
        else:
            return -1