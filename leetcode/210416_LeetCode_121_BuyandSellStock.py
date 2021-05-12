class Solution:
    def maxProfit(self, prices:list):
        if len(prices) == 1:
            return 0
        res = []
        buy = prices[0]
        for i in range(len(prices)-1):
            if buy >= prices[i+1]: # do not buy at time step i
               buy = prices[i+1]
            else:
                res.append(prices[i+1]-buy) # record profit

        return sorted(res)[-1] if len(res) > 0 else 0


s = Solution()
print(s.maxProfit([7,6,4,3,1]))