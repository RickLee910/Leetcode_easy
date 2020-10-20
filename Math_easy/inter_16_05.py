class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n != 0:
            temp = n // 5
            count += temp
            n = n // 5
        return count