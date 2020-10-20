class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, count  = 0, 1
        temp = []
        for i in range(1,len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                temp.append(count)
                count = 1
            if i == len(s) - 1:
                temp.append(count)
        for i in range(len(temp) - 1):
            ans += min(temp[i], temp[i + 1])
        return ans
s = Solution()
a ="00110011"
print(s.countBinarySubstrings(a))