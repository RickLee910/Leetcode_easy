class Solution:
    def flipAndInvertImage(self, A):
        size = (len(A[0]) + 1) // 2
        for j in range(len(A)):
            for i in range(size):
                A[j][i], A[j][-i - 1] = A[j][-i - 1], A[j][i]
                if A[j][-i - 1] > 0:
                    A[j][-i - 1] = 0
                else:
                    A[j][-i - 1] = 1
                if len(A[0]) % 2 == 1 and i ==size - 1:
                    break
                else:
                    if A[j][i] > 0:
                        A[j][i] = 0
                    else:
                        A[j][i] = 1
        return A
s = Solution()
a = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(s.flipAndInvertImage(a))
