import bisect
class Solution:
    #二分查找
    def countNegatives(self, grid) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        pos = n
        for i in range(m):
            l, r = 0, n - 1
            while l <= r:
                mid = (r + l) // 2
                if grid[i][mid] < 0:
                    pos = mid
                    r = mid - 1
                else:
                    l = mid + 1
            count += n - pos
        return count
#[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]


    #暴力法
    def countNegatives1(self, grid) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] >= 0:
                    count += 1
                else:
                    break
        return m*n - count
s= Solution()
a = [[3,2],[1,0]]
print(s.countNegatives(a))