# https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1

class Solution:
    def find(self, arr, n, x):
        if x not in arr:
            return -1,-1
        for i in range(n):
            if arr[i]==x:
                a=i
        for i in range(-1,-n,-1):
            if arr[i]==x:
                b=arr.index(arr[i])
                return b,a

if __name__ == '__main__':
    arr=[1, 3, 5, 5, 5, 5, 7, 123, 125,3 ]
    print(Solution().find(arr,len(arr),3))