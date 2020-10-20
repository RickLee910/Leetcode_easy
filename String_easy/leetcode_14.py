class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if strs == []:
            return ""
        j = len(strs[0])

        for i in range(j,0,-1):
            temp = strs[0][:i]
            for k in range(len(strs)):
                if strs[k][:i] != temp:
                    break
                if k == len(strs) - 1:
                    return temp
        return ""
s = Solution()
a = ["a"]
print(s.longestCommonPrefix(a))