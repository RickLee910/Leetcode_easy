class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        if N <= M:
            return M
        temp = '1' * (32 - j - 1) + '0'*(j - i + 1) + '1'*i
        return (int(temp, 2) & N) | (M<<i)
