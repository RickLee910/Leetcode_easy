class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        res = []
        for i in range(len(s)):
            if s[i] != " ":
                temp += s[i]
            if s[i] == " ":
                temp1 = list(reversed(temp)) + [s[i]]
                res += temp1
                temp = ""
            elif i == len(s) - 1:
                temp1 = list(reversed(temp))
                res += temp1

        return ''.join(res)
s = Solution()
a = ""
print(s.reverseWords(a))
