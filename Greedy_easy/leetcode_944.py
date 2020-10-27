class Solution:
    def minDeletionSize(self, A) -> int:
        l = 0
        for i in range(len(A[0])):
            j = 0
            while j < len(A) - 1:
                if A[j][i] > A[j+1][i]:
                    l += 1
                    break
                j+=1
        return l