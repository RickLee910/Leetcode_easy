class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        n, m = len(image), len(image[0])
        currColor = image[sr][sc]

        def dfs(x: int, y: int):
            if image[x][y] == currColor:
                image[x][y] = newColor
                for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                        dfs(mx, my)

        if currColor != newColor:
            dfs(sr, sc)
        return image

s = Solution()
a = [[1,1,1],[1,1,0],[1,0,1]]
print(s.floodFill(a,1,1,2))

