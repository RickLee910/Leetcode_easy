class Solution:
    #KMP
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp = (s * 2).index(s, 1)
        if temp != len(s):
            return True
        return False


    def repeatedSubstringPattern1(self, s: str) -> bool:
        i = 1
        temp = list(s)
        size = len(temp)

        while i <= size // 2:
            if size % i == 0 and i != 1:
                for j in range(size // i):
                    if temp[:i] != temp[j * i:(j + 1) * i]:
                        break
                    if j == size // i - 1:
                        return True
                i += 1
            elif i == 1:
                for j in range(size-1):
                    if temp[j] != temp[j+1]:
                        i += 1
                        break
                    if j == size - 2:
                        return True
            else:
                i += 1
        return False
s =Solution()
a ="a"
print(s.repeatedSubstringPattern(a))