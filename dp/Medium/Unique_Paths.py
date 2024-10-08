# Problem URL: https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        return self.check(m-1,n-1,dp)
    def check(self,i,j,dp):
        if i==0 and j==0:
            return 1

        if i<0 or j<0:
            return 0

        if dp[i][j] !=-1:
            return dp[i][j]

        up=self.check(i-1,j,dp)
        left=self.check(i,j-1,dp)

        dp[i][j]=up+left

        return dp[i][j]
