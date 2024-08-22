# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums=[]):
        a=[]
        for i in nums:
            a.append(i*i)
        for i in range(len(a)):
            for j in range(len(a)-i-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
        return a

if __name__ == '__main__':
    arr=[-3,35,6,4,-2]
    S=Solution()
    S.sortedSquares(arr)
        