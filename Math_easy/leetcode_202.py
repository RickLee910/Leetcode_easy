class Solution:
    def isHappy(self, n: int) -> bool:
        temp = []
        s = 0
        while s != 1:
            temp1 = list(str(n))
            for i in range(len(temp1)):
                s += int(temp1[i]) ** 2
            if s == 1:
                return True
            if s in temp:
                return False
            temp.append(s)
            n = s
            s = 0

s = Solution()
a = 19
print(s.isHappy(a))