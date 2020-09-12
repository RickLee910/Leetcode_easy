class Solution:
    #找到R坐标，利用方向数组进行循环，进行查找(更节省时间)
    def numRookCaptures(self, board):
        size = len(board)
        x, y = 0, 0
        zu_num = 0
        step = 0
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'R':
                    x, y = i, j
                    break
        dx, dy = [0,1,0,-1],[1,0,-1,0]
        for i in range(4):
            step = 0
            while True:
                tx = x + step * dx[i]
                ty = y + step * dy[i]
                if tx < 0 or tx >= 8 or ty < 0 or ty >= 8 or board[tx][ty] == 'B':
                    break
                if board[tx][ty] == 'p':
                    zu_num += 1
                    break
                step += 1

        return zu_num


    #自己的解法，先循环得出R的坐标，然后分别进行四个方向查找
    def numRookCaptures1(self, board):
        size = len(board)
        x,y = 0, 0
        zu_num = 0
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'R':
                    x, y = i, j
                    break
        for i in range(y + 1, size):
            if board[x][i] == 'p':
                zu_num += 1
                break
            if board[x][i] == 'B':
                break
        for i in range(x + 1, size):
            if board[i][y] == 'p':
                zu_num += 1
                break
            if board[i][y] == 'B':
                break
        for i in range(0, y):
            if board[x][y - i - 1] == 'p':
                zu_num += 1
                break
            if board[x][y - i - 1] == 'B':
                break
        for i in range(0, x):
            if board[x - i - 1][y] == 'p':
                zu_num += 1
                break
            if board[x - i - 1][y] == 'B':
                break
        return zu_num

sol = Solution()
a =[[".",".",".",".",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    ["p","p",".","R",".","p","B","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".","B",".",".",".","."],
    [".",".",".","p",".",".",".","."],
    [".",".",".",".",".",".",".","."]]
print(sol.numRookCaptures(a))
