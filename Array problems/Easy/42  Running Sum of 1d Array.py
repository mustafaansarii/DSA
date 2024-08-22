from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[]
        c_sum=0
        for i in nums:
            c_sum+=i
            result.append(c_sum)
        return result

if __name__ == '__main__':
    # Output: [1, 3, 6, 10]
    # Explanation: Running
    # sum is obtained as follows: [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4].
    # result = [1,3,6,10]
    nums = [1, 2, 3, 4]
    print(Solution().runningSum(nums))