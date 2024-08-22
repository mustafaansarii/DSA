# https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&category=Arrays&difficulty=School,Basic,Easy,Medium&sortBy=submissions
class Solution:
    def missingNumber(self,array,n):
        total_sum = n*(n+1)/2
        array_sum = sum(array)
        return int(total_sum-array_sum)

if __name__ == '__main__':
    S=Solution()
    arr=[1,2,3,4]
    print(S.missingNumber(arr,5))
