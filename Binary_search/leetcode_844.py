class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        temp = []
        for i in range(len(S)):
            if S[i] != '#':
                temp.append(S[i])
            else:
                if temp!=[]:
                    temp = temp[:-1]
        temp1 = []
        for i in range(len(T)):
            if T[i] != '#':
                temp1.append(T[i])
            else:
                if temp1 != []:
                    temp1 = temp1[:-1]
        return temp ==temp1