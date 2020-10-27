from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        temp1 = Counter(filter(str.isalpha,licensePlate.lower()))
        words = sorted(words, key=lambda x:len(x))
        for i in words:
            temp = temp1.copy()

            for j in i:
                if j in temp.keys():
                    if temp[j]>0:temp[j] -= 1
            if sum(temp.values()) == 0:
                return i
s = Solution()
a = "AN87005"

b = ["participant","individual","start","exist","above","already","easy","attack","player","important"]
print(s.shortestCompletingWord(a,b))