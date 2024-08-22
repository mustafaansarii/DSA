from typing import  List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            mid_value=nums[mid]
            if mid_value==target:
                return mid
            if nums[mid]>target:
                right=mid-1
            if nums[mid]<target:
                left=mid+1
        return left
if __name__ == '__main__':
    print(Solution().searchInsert([1,23,45,67,78],26))