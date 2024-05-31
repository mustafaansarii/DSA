# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = float('inf')
        INT_MIN = float('-inf')
        reverse = 0

        while x != 0:
            if reverse > INT_MAX / 10 or reverse < INT_MIN / 10:
                return 0
            elif x > 0:
                digit = x % 10
                reverse = reverse * 10 + digit
                x = x//10
            else:
                digit = x % -10
                reverse = reverse * 10 + digit
                x = x//10
                print(x)
        return reverse


if __name__ == '__main__':
    print(Solution().reverse(321))