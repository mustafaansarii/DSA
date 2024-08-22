# Problem: Maximum_Repeating_Number
# URL: https://www.geeksforgeeks.org/find-the-maximum-repeating-number-in-ok-time/

class Solution:
    def maxRepeating(self, k, arr):
        freq_Count = {}
        max_freq = 0
        max_num = 0

        for num in arr:
            freq_Count[num] = freq_Count.get(num, 0) + 1

            if freq_Count[num] > max_freq:
                max_freq = freq_Count[num]
                max_num = num
            elif freq_Count[num] == max_freq and num < max_num:
                max_num = num
        return max_num


if __name__ == '__main__':
    a=Solution().maxRepeating(3,[0,1,2,2])
    print(a)