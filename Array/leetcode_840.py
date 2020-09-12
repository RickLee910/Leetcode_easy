class Solution:
    def numMagicSquaresInside(self, grid):
        temp = 0
        count, judge = 0, 0
        if len(grid) <3 and len(grid[0]) < 3:
            return 0
        for i in range(1,len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                temp = grid[i][j - 1] + grid[i][j] + grid[i][j + 1]
                if grid[i - 1 ][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] == temp:
                    judge += 1
                if grid[i + 1 ][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1] == temp:
                    judge += 1
                if grid[i + 1 ][j - 1] + grid[i][j - 1] + grid[i - 1][j - 1] == temp:
                    judge += 1
                if grid[i + 1 ][j] + grid[i][j] + grid[i - 1][j] == temp:
                    judge += 1
                if grid[i + 1 ][j + 1] + grid[i][j + 1] + grid[i - 1][j + 1] == temp:
                    judge += 1
                if grid[i + 1 ][j + 1] + grid[i][j] + grid[i - 1][j - 1] == temp:
                    judge += 1
                if grid[i + 1 ][j - 1] + grid[i][j] + grid[i - 1][j + 1] == temp:
                    judge += 1
                if judge == 7:
                    count += 1
        return count
s = Solution()
a = [[8,1,6],[3,5,7],[4,9,2]]
print(s.numMagicSquaresInside(a))