class Solution:
    def islandPerimeter(self, grid) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp = 4
                    if i + 1 < len(grid) and grid[i + 1][j] == 1: temp -= 1
                    if i - 1 >= 0 and grid[i - 1][j] == 1: temp -= 1
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1: temp -= 1
                    if j - 1 >= 0 and grid[i][j - 1] == 1: temp -= 1
                    ans += temp
        return ans
s = Solution()
a = [[1,0]]
print(s.islandPerimeter(a))