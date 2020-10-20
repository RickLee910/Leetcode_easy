class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        if needle not in haystack:
            return -1
        else:
            i = 0
            for i in range(len(haystack)- len(needle) + 1) :
                if haystack[i:i + len(needle)] == needle:
                    break
            return i
s = Solution()
a = "mississippi"
b = "pi"
print(s.strStr(a,b))