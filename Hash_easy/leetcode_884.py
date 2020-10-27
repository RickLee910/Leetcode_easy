class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        tempA,tempB = {}, {}
        ans = []
        for i,x in enumerate(A.split()):
            tempA[x] = tempA.get(x, 0)+1
        for i,x in enumerate(B.split()):
            tempB[x] = tempB.get(x, 0)+1
        for i in list(tempA.keys()):
            if tempA[i] == 1 and i not in list(tempB.keys()):
                ans.append(i)
        for i in list(tempB.keys()):
            if tempB[i] == 1 and i not in list(tempA.keys()):
                ans.append(i)
        return ans