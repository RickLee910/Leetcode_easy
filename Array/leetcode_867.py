class Solution:
    def transpose(self, A):
        r_size = len(A)
        c_size = len(A[0])

        temp = [[0]*r_size for i in range(c_size)]
        for r in range(r_size):
            for c in range(c_size):
                temp[c][r] = A[r][c]
        return temp
sol = Solution()
a =[[1,2,3],[4,5,6],[7,8,9]]
print(sol.transpose(a))