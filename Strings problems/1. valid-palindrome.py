# https://leetcode.com/problems/valid-palindrome/description/
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        slist =re.findall("[a-z0-9]",s.casefold())
        return slist==slist[::-1]
if __name__ == '__main__':
    s=Solution()
    print(s.isPalindrome("This is book of mine!"))
    print(s.isPalindrome("A man, a plan, a canal: Panama"))