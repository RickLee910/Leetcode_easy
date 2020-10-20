class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minx,miny = 40000,40000
        if len(ops) == 0:
            return m * n
        for x, y in ops:
            minx = min(minx, x)
            miny = min(miny, y)
        return minx * miny