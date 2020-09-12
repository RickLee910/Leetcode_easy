import collections
class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if matrix == [] or matrix[0] == []:
             return False
        row = len(matrix)
        col = len(matrix[0])
        rows, column = 0, col - 1
        while rows < row and column >= 0:
            num = matrix[rows][column]
            if num == target:
                return True
            elif num > target:
                column -= 1
            else:
                rows +=1
        return False

    def findNumberIn2DArray1(self, matrix, target):
        if matrix == [] or matrix[0] == []:
             return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        for i in range(len(matrix)):
            temp = collections.Counter(matrix[i])
            if target in temp:
                return True
        return False


s = Solution()
a = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
print(s.findNumberIn2DArray(a, 5))