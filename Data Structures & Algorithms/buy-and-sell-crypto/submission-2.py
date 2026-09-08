class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxprof = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                prof = prices[sell] - prices[buy]
                maxprof = max(maxprof, prof)
            else:
                buy = sell
            sell += 1
        return maxprof