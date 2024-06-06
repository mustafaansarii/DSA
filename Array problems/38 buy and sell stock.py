class Solution:
    def maxProfit(self, prices) -> int:
        minimum=prices[0]
        maximum_profit=0
        for p in range(len(prices)):
            if prices[p]<minimum:
                minimum=prices[p]
            profit = prices[p] - minimum
            if profit>maximum_profit:
                maximum_profit=profit

        return maximum_profit


if __name__ == '__main__':
    array=[7,1,5,3,6,4]
    print(Solution().maxProfit(array))
