import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp = collections.Counter(s)
        for i in range(len(s)):
            if temp[s[i]] == 1:
                return i
        return -1