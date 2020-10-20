class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '' or s.isspace():
            return 0
        count = 0
        for i in range(len(s) - 1,-1,-1):
            if not s[i].isspace():
                while not s[i - count].isspace():
                    count += 1
                    if count == len(s):
                        break
                return count
s = Solution()
a = "a"
print(s.lengthOfLastWord(a))