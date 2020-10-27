class Solution:
    def findContentChildren(self, g, s) -> int:
        if len(s) == 0:
            return 0
        ans = 0
        g.sort()
        s.sort()
        j,i = 0,0
        while i < len(g):
            if s[j] >= g[i]:
                ans += 1
                j += 1
                i += 1
            else:
                j += 1
            if j == len(s):
                break
        return ans
