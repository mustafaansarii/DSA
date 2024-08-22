from typing import  List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        while i<=j and j<len(nums):
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
        return i+1

if __name__ == '__main__':
    arr=[0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(arr))