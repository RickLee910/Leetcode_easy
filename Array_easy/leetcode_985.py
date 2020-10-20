class Solution:
    def sumEvenAfterQueries(self, A, queries):
        ans = []
        He = 0
        size = len(queries)
        if size == 0:
            return A
        size1 = len(A)
        for i in range(size1):
            if A[i] %2 == 0:
                He += A[i]
        for i in range(size):
            if A[queries[i][1]] % 2 == 1 and (A[queries[i][1]] +queries[i][0]) % 2 == 0:
                A[queries[i][1]] += queries[i][0]
                He += A[queries[i][1]]
            elif A[queries[i][1]] % 2 == 0 and (A[queries[i][1]] +queries[i][0]) % 2 == 1:
                He -= A[queries[i][1]]
                A[queries[i][1]] += queries[i][0]
            elif A[queries[i][1]] % 2 == 0 and (A[queries[i][1]] +queries[i][0]) % 2 == 0:
                A[queries[i][1]] += queries[i][0]
                He += queries[i][0]
            else:
                A[queries[i][1]] += queries[i][0]
            ans.append(He)
        return ans
s = Solution()
a =[3,2]
b =[[4,0],[3,0]]
print(s.sumEvenAfterQueries(a,b))