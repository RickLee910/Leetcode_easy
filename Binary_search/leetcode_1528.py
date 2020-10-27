class Solution:
    def restoreString(self, s: str, indices) -> str:
        temp = {}
        i = 0
        while i < len(s):
            temp[indices[i]] = s[i]
            i+=1
        ans = []
        for i in range(len(temp)):
            ans.append(temp[i])
        return ''.join(ans)