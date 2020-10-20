class Solution:
    def climbStairs(self, n: int) -> int:
        def fac(n):
            if n == 1 or n == 0:
                return 1
            return n * fac(n-1)
        temp = {}
        temp[1] = n - 2
        temp[2] = 1
        S = 1
        while temp[1] >= 0:
            S += fac(temp[1] + temp[2]) // (fac(temp[2])*fac(temp[1]))
            temp[1] -= 2
            temp[2] += 1

        return S
s = Solution()
a = 3
print(s.climbStairs(a))
