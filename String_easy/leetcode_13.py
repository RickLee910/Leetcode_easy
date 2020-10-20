class Solution:
    def romanToInt(self, s: str) -> int:
        Romen = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = Romen[s[-1]]
        if len(s) == 1:
            return Romen[s]
        for i in range(len(s) - 1):
            if Romen[s[i]] >= Romen[s[i+1]]:
                ans += Romen[s[i]]
            else:
                ans -= Romen[s[i]]
        return ans
s = Solution()
a ="DM"
print(s.romanToInt(a))