class Solution:
    def validMountainArray(self, A):
        left = 0
        if len(A) < 3:
            return False
        for i in range(len(A) - 1):
            if A[i + 1] == A[i]:
                return False
            elif A[i + 1] < A[i]:
                left = i
                break
        if left == 0:
            return False
        for j in range(left, len(A) - 1):
            if A[j + 1] >= A[j]:
                return False
        return True

sol = Solution()
a=[9,8,7,6,5,4,3,2,1,0]
print(sol.validMountainArray(a))