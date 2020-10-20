class Solution:
    def kWeakestRows(self, mat, k):
        n = len(mat)
        power = [sum(line) for line in mat]
        ans = list(range(n))
        ans.sort(key=lambda i: (power[i], i))
        return ans[:k]

    def kWeakestRows1(self, mat, k):
        size_row = len(mat)
        size_col = len(mat[0])
        res = {}
        temp2 = []
        for i in range(size_row):
            temp = 0
            while temp < size_col:
                if mat[i][temp] == 1:
                    temp += 1
                else:
                    break
            res[i] = temp
        temp1 = sorted(list(res.values()))
        for i in range(k):
            temp2.append(list(res.keys())[list(res.values()).index(temp1[i])])
            res[temp2[i]] = -1
        return temp2
s = Solution()
a = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
print(s.kWeakestRows(a,4))