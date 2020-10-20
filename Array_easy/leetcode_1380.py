import numbers
class Solution:
    def luckyNumbers (self, matrix):
        temp = []

        row = list(min(matrix[i]) for i in range(len(matrix)))
        col = list(max([j[i] for j in matrix])for i in range(len(matrix[0])))
        if len(row) >= len(col):
            for i in range(len(col)):
                if col[i] in row:
                    temp.append(col[i])
        else:
            for i in range(len(row)):
                if row[i] in col:
                    temp.append(row[i])
        return temp


x = [[7,8],[1,2]]
sol = Solution()
print(sol.luckyNumbers(x))
