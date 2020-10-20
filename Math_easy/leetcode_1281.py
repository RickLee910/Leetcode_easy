class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = list(str(n))
        T = 1
        S = 0
        for i in temp:
            T *= int(i)
            S += int(i)
        return T - S