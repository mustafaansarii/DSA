# Problem URL: https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/
class Solution:
    def matrixMultiplication(self,arr, n):
        dp=[[-1 for _ in range(n)]for _ in range(n)]
        return self.MCM(1,n-1,arr,dp)

    def MCM(self,i,j,arr,dp):
        if i==j:
            return 0
        
        dp[i][j]=float("inf")

        if dp[i][j]!=-1:
            dp[i][j]

        for k in range(i,j):
            cost=self.MCM(i,k,arr,dp)+self.MCM(k+1,j,arr,dp)+arr[i-1]*arr[k]*arr[j]
            dp[i][j]=min(dp[i][j],cost)
        
        return dp[i][j]

N = 5
arr =[40, 20, 30, 10, 30]

print(Solution().matrixMultiplication(arr,N))
        

