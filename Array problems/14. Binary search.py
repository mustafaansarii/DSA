
class Solution:
    def search(self, nums, target):

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

if __name__ == '__main__':
    arr=[1,2,3,4,5,67,88]
    print(Solution().search(arr,4))