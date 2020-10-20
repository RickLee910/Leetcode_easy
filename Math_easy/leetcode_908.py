class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if len(A) == 1:
            return 0
        A.sort()
        temp = A[-1] - A[0] - abs(2 * K)
        return temp if temp > 0 else 0 