from collections import Counter
class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1):
            temp_0 = Counter(s[0:i+1])['0']
            temp_1 = Counter(s[i+1:])['1']
            ans = max(ans, temp_0 + temp_1)
        return ans
s = Solution()
a = '01'
print(s.maxScore(a))