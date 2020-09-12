class Solution:
    def imageSmoother(self, M):
        row = len(M)
        col = len(M[0])
        temp = [[0] * col for i in range(row)]
        for i in range(row):
            for j in range(col):
                count = 0
                for r in (i - 1, i , i + 1):
                    for c in (j-1, j, j + 1):
                        if c >=0 and c <col and r < row and r >= 0:
                            temp[i][j] += M[r][c]
                            count += 1
                temp[i][j] //= count
        return temp
s= Solution()
a = [[1,1,1],
 [1,0,1],
 [1,1,1]]
print(s.imageSmoother(a))