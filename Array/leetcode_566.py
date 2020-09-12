class Solution:
    #个人改进版
    def matrixReshape(self, nums, r, c):
        row = len(nums)
        col = len(nums[0])
        temp = [[int] * c for i in range(r)]
        count = 0
        if row * col == r * c:
            for i in range(row):
                for j in range(col):
                    temp[count // c][count % c] = nums[i][j]
                    count += 1
            return temp
        else:
            return nums



    #个人
    def matrixReshape1(self, nums, r, c):
        h = len(nums)
        l = len(nums[0])
        temp = [[0] * c for i in range(r)]
        A = []
        if r * c == h * l:
            for i in range(h):
                for j in range(l):
                    A.append(nums[i][j])
            count = 0
            for i in range(r):
                for j in range(c):
                    temp[i][j] = A[count]
                    count += 1
            return temp
        else:
            return nums


sol = Solution()
A=[[1,2],
 [3,4]]
print(sol.matrixReshape(A,4,1))
