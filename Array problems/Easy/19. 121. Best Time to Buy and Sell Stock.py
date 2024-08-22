# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices) -> int:
        x=[]
        a=min(prices)
        c=prices.index(a)
        for i in range(c,len(prices)):
            x.append(prices[i])
        return max(x)-a




if __name__ == '__main__':
    list1=[7,1,5,3,6,4]
    a=Solution().maxProfit(list1)
    print(a)

