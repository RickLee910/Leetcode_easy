class Solution:
    #升级
    def isPathCrossing(self, path: str) -> bool:
        dirs = {
            "N": (-1, 0),
            "S": (1, 0),
            "W": (0, -1),
            "E": (0, 1),
        }

        x, y = 0, 0
        vis = set([(x, y)])
        for ch in path:
            dx, dy = dirs[ch]
            x, y = x + dx, y + dy
            if (x, y) in vis:
                return True
            vis.add((x, y))

        return False
    #原始
    def isPathCrossing1(self, path: str) -> bool:
        point = [[0,0]]
        x,y = 0,0
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'E':
                x += 1
            elif i == 'W':
                x -= 1
            else:
                y -= 1
            if [x,y] in point:
                return True
            else:
                point.append([x, y])
        return False
s = Solution()
a = "NESW"
print(s.isPathCrossing(a))