# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    def findDuplicate(self, nums) -> int:

        my_dict = {}

        for element in nums:

            if element not in my_dict:
                my_dict[element] = 0

            else:
                return element

        return -1


if __name__ == '__main__':
    array=[1,3,4,2,2]
    print(Solution().findDuplicate(array))