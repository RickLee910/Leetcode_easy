from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        temp = Counter(moves)
        return temp['U'] == temp['D'] and temp['R'] == temp['L']
s = Solution()
a = ''
print(s.judgeCircle(a))