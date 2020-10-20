class Solution:
    #优化
    def makeGood(self, s: str) -> str:
        temp = []
        for i in s:
            temp.append(i)
            if len(temp) >= 2 and abs(ord(temp[-1]) - ord(temp[-2])) == 32:
                temp = temp[0:-2]
        return ''.join(temp)

    #原始
    def makeGood1(self, s: str) -> str:
        ls = list(s)
        if len(ls) == 1:
            return s
        left, i = 0, 1
        while i < len(ls):
            if abs(ord(ls[left]) - ord(ls[i])) == 32:
                ls.pop(i)
                ls.pop(left)
                if left != 0:
                    i = left
                    left -= 1
                else:
                    i, left = 1, 0
            else:
                left += 1
                i += 1
        return ''.join(ls[0:])
s =Solution()
a = "djrDdRJD"
print(s.makeGood(a))