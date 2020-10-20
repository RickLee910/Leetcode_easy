class Solution:
    def getRow(self, rowIndex):
        row = [1]
        for i in range(1, rowIndex + 1):
            row.insert(0, 0)
            for j in range(i):
                row[j] = row[j] + row[j + 1]
        return row


    def getRow1(self, rowIndex: int):
        if rowIndex == 1:
            return [1]
        if rowIndex == 2:
            return [1,1]
        res = [[1]*(rowIndex + 1) for i in range(rowIndex +1)]
        for i in range(2,rowIndex + 1):
            for j in range(1,i):
                res[i][j] =res[i - 1][j - 1] + res[i - 1][j]
        return res[-1]
s= Solution()
a = 3
print(s.getRow(a))