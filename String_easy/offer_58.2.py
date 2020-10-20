class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        S = list(s)
        S += S[:n]
        del S[:n]

        return ''.join(S)
s = Solution()
a = "abcdefg"
b = 2
print(s.reverseLeftWords(a,b))