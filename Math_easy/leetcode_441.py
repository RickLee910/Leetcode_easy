class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        for i in range(1, n):
            if n < i * (1 + i) // 2:
                return i - 1
            elif n == i * (1 + i) // 2:
                return i
