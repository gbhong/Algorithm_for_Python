class Solution:
    def maxProfit(self, prices: list):
        if len(prices) == 1:
            return 0
        else:
            sell_idx, sell = max(list(enumerate(prices[1:], start=1)), key=lambda x:(x[1], x[0]))
            buy = min(prices[:sell_idx])
            return (sell-buy) if sell > buy else 0

s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))