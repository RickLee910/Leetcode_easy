class Solution:
    def commonChars(self, A):
        if not A:
            return []
        res = []
        for c in set(A[0]):
            count = [w.count(c) for w in A]
            s = c * min(count)  # 如果不是每个单词都有的字母，min(count)=0
            res.extend(s)
        return res


sol = Solution()
a = ["bella","label","roller"]

print(sol.commonChars(a))