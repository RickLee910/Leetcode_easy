class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a' * n
        else:
            return 'a' * (n - 1) + 'b'
s = Solution()
a = 6
print(s.generateTheString(a))