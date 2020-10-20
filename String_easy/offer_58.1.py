class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        temp.reverse()
        return ' '.join(temp)
s = Solution()
a = "  hello world!  "
print(s.reverseWords(a))