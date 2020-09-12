class Solution:
    def maxProfit(self, prices) -> int:
        left, right =0, 0
        ans = 0
        left_found = False
        if len(prices) == 2:
            return (prices[1] - prices[0] if prices[1] >= prices[0] else 0)
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1] and not left_found:
                left = i - 1
                left_found = True
            if prices[i] < prices[i - 1] and left_found:

                right = i - 1
                if right > left:
                    ans += prices[right] - prices[left]
                    left = i
                    left_found = False
            if i == len(prices) - 1:
                right = i
                if prices[right] < prices[left]:
                    break
                else:
                    ans += prices[right] - prices[left]
        return ans
s = Solution()
a = [2,1,4]
print(s.maxProfit(a))