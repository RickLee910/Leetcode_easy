class Solution:
    def sortArrayByParity(self, A):
        left = 0
        temp = []
        for i in range(len(A)):
            while A[i] % 2 == 1:
                A[i], A[-1] = A[-1], A[i]
                if A[i] % 2 == 1:
                    continue
                else:
                    i+=1

        return A
sol = Solution()
a = [3,1,2,4]
print(sol.sortArrayByParity(a))

