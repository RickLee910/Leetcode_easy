from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        temp = Counter(text)
        ins = Counter('balloon')
        count = temp['b'] // ins['b']
        for i in list(ins.keys()):
            count = min(count, temp[i] // ins[i])
        return count
s = Solution()
a = "lonbalxballpoon"
print(s.maxNumberOfBalloons(a))
