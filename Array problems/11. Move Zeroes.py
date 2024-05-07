# https://leetcode.com/problems/move-zeroes/description/

def moveZeroes(nums):
    n = len(nums)
    i = 0
    for j in range(n):
        if (nums[j] != 0):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

if __name__ == '__main__':
    nums=[0,-1,3,6,0]
    moveZeroes(nums)
    print( nums)