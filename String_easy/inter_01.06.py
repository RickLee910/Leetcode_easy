from collections import Counter
class Solution:
    def compressString(self, S: str) -> str:
        if len(S) == 1:
            return S
        ans = []
        count = 1
        for i in range(len(S) - 1):
            if S[i] == S[i + 1]:
                count += 1
            else:
                ans.append(S[i] + str(count))
                count = 1
            if i == len(S) - 2:
                ans.append(S[i + 1] + str(count))
                count = 1
        res = ''.join(ans)

        return (res if len(res) < len(S) else S)
s = Solution()
a = "a"
print(s.compressString(a))