class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxprof = 0
        for buy in range(len(prices) - 1):
            for sell in range(buy + 1, len(prices)):
                if prices[buy] > prices[sell]:
                    continue
                if prices[sell] - prices[buy] > maxprof:
                    maxprof = prices[sell] - prices[buy]
        return maxprof