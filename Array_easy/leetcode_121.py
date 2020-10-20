class Solution:
    def maxProfit(self, prices) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit


s = Solution()
a = [11,2,7,1,4]
print(s.maxProfit(a))