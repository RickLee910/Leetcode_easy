class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        temp = str2 + str1
        min_l = min(len(str1), len(str2))
        for i in range(min_l + 1,0,-1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                count = len(temp) // i
                temp1=1
                for j in range(0,len(temp) - i, i):
                    if temp[j:j + i] != temp[j + i: j + 2 * i]:
                        break
                    temp1 += 1
                if temp1 == count:
                    return temp[:i]
            else:
                continue
        return ''
s = Solution()
a = "ABABABAB"
b = "ABAB"
print(s.gcdOfStrings(a,b))