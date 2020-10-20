class Solution:
    def isBoomerang(self, points) -> bool:
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        temp1 = (points[1][0] - points[0][0])* (points[2][1] - points[1][1])
        temp2 = (points[2][0] - points[1][0])* (points[1][1] - points[0][1])
        return  temp1 != temp2
s = Solution()
a = [[0,1],[1,1],[0,0]]
print(s.isBoomerang(a))