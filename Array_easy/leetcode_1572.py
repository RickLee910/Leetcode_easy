class Solution:
    def diagonalSum(self, mat) -> int:
        if len(mat) == 1:
            return mat[0][0]
        count = 0
        n = len(mat)
        if n % 2 == 1:
            count -= mat[n // 2][n // 2]
        for i in range(n):
            count += mat[i][i]
            count += mat[i][n - 1 - i]
        return count