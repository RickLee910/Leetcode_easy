class Solution:
    #连线法，利用枚举巧妙将二维数组坐标化，然后判断在字典中的同一直线上的数是否相等
    def isToeplitzMatrix(self, matrix):
        group = {}
        for r, row in enumerate(matrix):
            for c, value in enumerate(row):
                if r- c not in group:
                    group[r - c] = value
                elif group[r - c] != value:
                    return False
        return True

    #左上角法，判断第一行之外的数的左上角是否和其一致，利用all函数进行判断
    def isToeplitzMatrix1(self, matrix):
        return all(r == 0 or c == 0 or matrix[r - 1][c - 1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))




col = Solution()
a=[
  [1,3,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
print(col.isToeplitzMatrix(a))
