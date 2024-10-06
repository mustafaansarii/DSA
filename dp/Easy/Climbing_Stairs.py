# Problem URL: https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climStair(self, n):
        if n==1:
            return 1
        if n==2:
            return 2
        # a=1
        # b=2
        # for i in range(3,n+1):
        #     a,b=b,a+b
        # return b

        memo=[-1]*(n+1)
        memo[1]=1
        memo[2]=2
        for i in range(3,n+1):
            memo[i]=memo[i-1]+memo[i-2]
        return memo[n]
    

    



print(Solution().climStair(68))