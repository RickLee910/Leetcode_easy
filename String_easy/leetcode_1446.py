class Solution:
    def maxPower(self, s: str) -> int:
        dp, max_c = 1, 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp += 1
                max_c = max(max_c, dp)
            else:
                dp = 1
        return max_c
s = Solution()
a = ""
print(s.maxPower(a))