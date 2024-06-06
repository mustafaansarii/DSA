class Solution(object):
    def twoSum(self, arr, target):
        for j in range(len(arr)-1):
            for i in range(j+1,len(arr)):
                if arr[j]+arr[i]==target:
                    return j,i


if __name__ == '__main__':
    arr=[3,2,3]
    k=6
    print(Solution().twoSum(arr,k))
