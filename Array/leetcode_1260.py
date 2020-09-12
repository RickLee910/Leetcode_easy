class Solution:
    def shiftGrid(self, grid, k):
        temp = [0] * k
        res = [[0] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            temp.extend(grid[i])
        for i in range(k):
            temp[k -i-1] = temp[- 1]
            temp.pop()
        for i in range(len(grid)):
            res[i] = [temp[j] for j in range(len(grid[0]) * i, len(grid[0]) * (i + 1))]
        return res
s = Solution()
a = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
print(s.shiftGrid(a, 4))
