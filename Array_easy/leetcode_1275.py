class Solution:
    def tictactoe(self, moves):
        wins = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]

        def checkwin(S):
            for win in wins:
                flag = True
                for pos in win:
                    if pos not in S:
                        flag = False
                        break
                if flag:
                    return True
            return False

        A, B = set(), set()
        for i, (x, y) in enumerate(moves):
            if i % 2 == 0:
                A.add((x, y))
                if checkwin(A):
                    return "A"
            else:
                B.add((x, y))
                if checkwin(B):
                    return "B"

        return "Draw" if len(moves) == 9 else "Pending"

s = Solution()
a =[[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
print(s.tictactoe(a))