class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        currcolor = image[sr][sc]
        def dfs(x, y):
            if 0<= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == currcolor:
                image[x][y] = newColor
                dfs(x+1,y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
        if currcolor != newColor:
            dfs(sr,sc)
        return image
s = Solution()
a = [[0,0,0],[0,0,0]]
print(s.floodFill(a,0,0,2))

