class Solution:
    def checkStraightLine(self, coordinates):
        size = len(coordinates)
        is_y = 1
        for i in range(size - 1):
            if coordinates[i+ 1][0] - coordinates[i][0] == 0:
                is_y += 1
            else:break
        if is_y == size:
            return True
        elif is_y > 1:
            return False
        slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i in range(1, size - 1):
            if (coordinates[i + 1][1] - coordinates[i][1]) != slope * (coordinates[i + 1][0] - coordinates[i][0]):
                return False
        return True

sol = Solution()
a = [[1,1],[2,2],[2,0]]
print(sol.checkStraightLine(a))