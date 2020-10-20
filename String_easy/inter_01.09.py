class Solution:
    #切片比较
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        return s1 in (s2 + s2)
    #循环判断
    def isFlipedString1(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == '' and s2 == '':
            return True
        S2 = list(s2)
        S1= list(s1)
        for i in range(len(s2)):
            if S2 == S1:
                return True
            else:
                S2.append(S2.pop(0))
        return False
s = Solution()
a = "waterbottl1"
b = "erbottlewat"
print(s.isFlipedString(a,b))