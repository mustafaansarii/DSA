class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        words=S.split('.')
        reversed_word=words[::-1]
        reversed='.'.join(reversed_word)
        return reversed

s="i.like.this.program.very.much"
print(Solution().reverseWords(s))
