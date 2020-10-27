class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        temp = {}
        for i in range(R):
            for j in range(C):
                d = abs(i - r0) + abs(j - c0)
                if d in temp.keys():
                    temp[d].append([i,j])
                else:
                    temp[d] = [[i,j]]
        ans = []
        temp1 = sorted(list(temp.keys()))
        for i in temp1:
            for j in temp[i]:
                ans.append(j)
        return ans
s = Solution()
print(s.allCellsDistOrder(2,3,1,2))