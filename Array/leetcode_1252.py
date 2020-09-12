import collections
class Solution:
    def oddCells(self, n: int, m: int, indices) -> int:
        row = [0] * n
        col = [0] * m
        for x, y in indices:
            row[x] += 1
            col[y] += 1
        odd_row = sum(x % 2 == 1 for x in row)
        odd_col = sum(x % 2 == 1 for x in col)
        return odd_row* (m - odd_col) + (n - odd_row) * odd_col