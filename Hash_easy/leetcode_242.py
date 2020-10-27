class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1,temp2 = {},{}
        for i,x in enumerate(s):
            temp1[x] = temp1.get(x,0) + 1
        for i,x in enumerate(t):
            temp2[x] = temp2.get(x,0) + 1
        return temp1 == temp2