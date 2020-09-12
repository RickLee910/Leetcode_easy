class Solution:
    def sortedSquares(self, A):
        var = 0
        for i, value in enumerate(A):
            A[i] = value * value
        A.sort()
        return A



sol = Solution()
a = [-2, 0]
print(sol.sortedSquares(a))