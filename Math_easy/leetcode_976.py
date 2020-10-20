class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        A = A[::-1]
        maxl = 0
        for i in range(len(A) - 2):
            if A[i + 2] + A[i + 1] > A[i]:
                maxl = max(maxl, A[i] + A[i + 1] + A[i + 2])

        return maxl