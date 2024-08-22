class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max=-1
        for i in range(len(nums)):
            if nums[i]>max:
                max=nums[i]
        return max
