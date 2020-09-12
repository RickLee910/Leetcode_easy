class Solution:
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A

s = Solution()
a = [648,831,560,986,192,424,997,829,897,843]
print(s.sortArrayByParityII(a))

