#https://www.geeksforgeeks.org/problems/square-root/1
#Complete this function
#Complete this function
class Solution:
    def floorSqrt(self, n): 
        #Your code here
        left=0
        right=n
        ans=0
        while left<=right:
            mid=left+(right-left)//2
            sq=mid*mid
            if sq==n:
                return mid
            elif sq<n:
                ans=mid
                left=mid+1
            else:
                right=mid-1
                
        return ans
        


if __name__=="__main__":
    a=Solution().floorSqrt(23)
    print(a)
    