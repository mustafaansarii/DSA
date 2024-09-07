class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum / k

if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    s = Solution()
    print(s.findMaxAverage(nums, k))  
