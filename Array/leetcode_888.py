class Solution:
    def fairCandySwap(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]



sol = Solution()
A = [1,2,5]
B = [2,4]
print(sol.fairCandySwap(A, B))