class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        if t == '' and s != '':
            return False
        temps = list(s)
        tempt = list(t)

        j = 0
        for i in range(len(tempt)):
            if tempt[i] == temps[j]:
                j += 1
                if j == len(temps):
                    return True
        return False