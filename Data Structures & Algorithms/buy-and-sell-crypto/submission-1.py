class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for buy in range(0,n):
            for sell in range(buy+1,n):
                if prices[sell]>prices[buy]:
                    profit = prices[sell]-prices[buy]
                    max_profit = max(max_profit,profit)

        return max_profit 

            



        