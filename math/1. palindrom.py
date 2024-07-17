class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = 0
        c = 0
        new = x
        while x>temp:
            c = x % 10
            x //= 10
            temp = temp * 10 + c
        if temp == new:
            return True
        else:
            return False

if __name__ == '__main__':
    x=121
    print(Solution().isPalindrome(x))
