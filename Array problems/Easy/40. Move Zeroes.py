class Solution:
    def moveZeroes(self, nums):
        j=0
        for i in range(len(nums)):
            if arr[i]!=0:
                arr[j],arr[i]=arr[i],arr[j]
                j+=1
        return nums


if __name__ == '__main__':
    arr=[0,1,0,3,12]
    print(Solution().moveZeroes(arr))