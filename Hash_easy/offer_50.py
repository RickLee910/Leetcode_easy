class Solution:
    def firstUniqChar(self, s: str) -> str:
        temp = {}
        for i,x in enumerate(s):
            temp[x] =temp.get(x,0)+1
        for i in temp.keys():
            if temp[i] == 1:
                return i
        return ' '