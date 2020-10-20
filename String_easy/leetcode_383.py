from collections import deque
from collections import Counter
class Solution:
    #不按顺序
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)
        for i in list(ran.keys()):
            if not mag[i] or mag[i] < ran[i]:
                return False
        return True

    #按顺序计算
    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == '':
            return True
        mag = list(magazine)
        temp = deque()
        j = 0
        for i in range(len(mag)):
            if mag[i] == ransomNote[j]:
                temp.append(mag[i])
                j += 1
                if j == len(ransomNote):
                    return True
            else:
                if temp:
                    temp.popleft()
                j = 0
        return False
s = Solution()
a = 'aab'
b = 'abb'
print(s.canConstruct(a,b))