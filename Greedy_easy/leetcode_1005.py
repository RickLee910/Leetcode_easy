class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        A.sort()
        l_minus = 0

        for i in A:
            if i < 0:
                l_minus += 1
            else: break
        l_positive = len(A) - l_minus
        if K < l_minus:
            return abs(sum(A[:K])) + sum(A[K:])
        else:
            if (K - l_minus) % 2 ==0:
                return abs(sum(A[:l_minus])) + sum(A[l_minus:])
            else:
                if len(A) - l_minus >0:
                    return abs(sum(A[:l_minus])) + sum(A[l_minus:]) - 2 * min(abs(A[l_minus - 1]),A[l_minus])
                else:
                    return abs(sum(A[:l_minus]))


s = Solution()
a = [-8,3,-5,-3,-5,-2]
print(s.largestSumAfterKNegations(a,6))