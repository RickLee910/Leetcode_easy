class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        temp = {}
        ans = 0
        for i,x in enumerate(S):
            temp[x] = temp.get(x,0) + 1
        for i in temp.keys():
            if i in J:
                ans += temp[i]
        return ans
s = Solution()
a = "aA"
b = "aAAbbbb"
print(s.numJewelsInStones(a,b))