class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        if n == 3:
            return 4
        a, b, c = 1, 2, 4
        for i in range(3, n + 1):
            a, b, c = b, c, (a + b + c) % (1000000007)



        return c
s = Solution()
a = 5
print(s.waysToStep(a))